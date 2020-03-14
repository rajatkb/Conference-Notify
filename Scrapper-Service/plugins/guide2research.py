from typing import List, Dict

import requests
from bs4 import BeautifulSoup as bs

import logging
from commons import PageParsingError, Scrapper
from datamodels import Conference, Metadata


class Guide2ResearchScrapper(Scrapper):
    def __init__(self, **config):
        super().__init__(context_name=__name__, **config)
        self.base_address = "http://www.guide2research.com/topconf/"
        self.site_name = "guide2research"

    def extract_and_push(self):
        '''
        Main calling method for g2r scraper
        Collects the links of all top conferences available
        and posts them to db
        '''
        conference_links = self._get_conferences_list()
        for link in conference_links:
            try:
                conf_data = self._parse_conference(link=link)
                self.push_todb(conf_data)
            except Exception as e:
                self.logger.error(
                    f'Error while parsing page {link}, find full trace {e}')

    def parse_action(self):
        self.extract_and_push()

    def _get_conferences_list(self) -> List[str]:
        '''
        parses topconferences baseurl and returns -
        - a list of available links
        '''
        base_address = self.base_address
        try:
            page = requests.get(base_address)
            if page.status_code == 200:
                content = page.content
        except Exception as e:
            PageParsingError(
                f"The following error occured when trying to parse a page {e}")
        return self._parse_base(content)

    def _parse_base(self, content: bytes) -> List[str]:
        '''
        Wrapper to parse the `/topconf` page and returns
        a list of links for active conferences

        Args:
        content: bytes

        Returns:
        list of conferences: list
        '''
        soup = bs(content, 'html5lib')
        div_el = soup.find('div', attrs={'id': 'ajax_content'})
        conf_tables = div_el.findAll('table')
        links = []
        for table in conf_tables:
            anchor = table.h4.a
            if not anchor:
                pass
            else:
                link = f"http://www.guide2research.com{anchor['href']}"
                links.append(link)
        return links

    def _parse_conference(self, link: str) -> Conference:
        '''
        Parses individual conference page and,
        return Conference object

        Args:
        ---
        link: str

        Returns:
        ---
        Conference: object
        '''
        try:
            page = requests.get(link, allow_redirect=True)
            if page.status_code == 200:
                content = page.content
        except Exception as e:
            PageParsingError(
                f'The following error occured while parsing a page {e}')
        soup = bs(content, 'html5lib')
        post_div = soup.find('div', attrs={'class': 'single_post'})
        post_tables = post_div.find_all('table')
        title = soup.h1.text
        conf_info = self._get_top_conf_info(table=post_tables[0])
        rating_info = self._get_top_conf_ranking(table=post_tables[1])
        bulk_text = self._get_bulk_text(soup)
        url = conf_info.get('link')
        deadline = conf_info.get('deadline')
        metadata = {}
        metadata['dates'] = conf_info['dates']
        metadata['rankings'] = rating_info
        return Conference(title=title,
                          url=url,
                          deadline=deadline,
                          metadata=metadata,
                          **{"bulkText": bulk_text})

    def _get_top_conf_info(self, table: bs) -> Dict[str, object]:
        '''
        Parses conference info table and
        returns information dictionary

        Args:
        ---
        table: bs4 table

        Returns:
        ---
        conference information dictionary
        '''
        tds = table.findAll('td')
        deadline = tds[1].text.strip()
        dates = tds[4].text.strip().split('-')
        address = tds[6].text.strip()
        link = tds[8].text.strip()
        return ({'deadline': deadline,
                 'dates': dates,
                 'address': address,
                 'link': link})

    def _get_top_conf_ranking(self, table: bs) -> Dict['str', 'str']:
        '''
        Parses conference ranking info table and
        returns ranking information dictionary

        Args:
        ---
        table: bs4 table

        Returns:
        ---
        conference ranking information dictionary
        '''
        tds = table.findAll('td')
        g2rranking = tds[2].text
        category_a = tds[5].text.strip()
        category_a_value = tds[6].text.strip()
        category_b = tds[7].text.strip()
        category_b_value = tds[8].text.strip()
        category_c = tds[9].text.strip()
        category_c_value = tds[10].text.strip()
        hindex = tds[-1].font.text
        return ({'Guide2Research Overall Ranking': g2rranking,
                 category_a: category_a_value,
                 category_b: category_b_value,
                 category_c: category_c_value,
                 'g_scholar_h5_index': hindex})

    def _get_bulk_text(self, soup: bs) -> str:
        '''
        Parses page soup and returns bulk text

        Args:
        ---
        soup: bs4 soup

        Returns:
        ---
        bulk text: str
        '''
        paragraphs = soup.find_all('p')
        bulk_text = paragraphs[0] + paragraphs[1]
        return bulk_text