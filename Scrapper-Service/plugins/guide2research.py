import logging
from datetime import datetime as dt
from typing import Dict, List
import itertools
import requests
from bs4 import BeautifulSoup as bs

from commons import PageParsingError, Scrapper
from datamodels import Conference, Metadata


class Guide2ResearchScrapper(Scrapper):
    def __init__(self, **config):
        super().__init__(context_name=__name__, **config)
        self.base_address = "http://www.guide2research.com"
        self.top_conf_address = self.base_address + "/topconf/"
        self.all_confs_base_address = self.base_address + "/conferences/"
        self.all_conf_page_links = [self.all_confs_base_address]
        self.all_conf_page_count = 1
        self.site_name = __name__
        self.scrapper_name = "Guide2Research"

    def parse_action(self):
        self.extract_and_push()

    def extract_and_push(self):
        """
        Main calling method for g2r scraper
        Collects the links of all top conferences available
        and posts them to db
        """
        top_conference_links = self._get_conferences_list(which='top')
        all_conference_links = self._get_conferences_list(which='all')
        for i, link in enumerate(top_conference_links):
            try:
                conf_data = self._parse_top_conference(link=link)
                if not conf_data:
                    pass
                else:
                    self.push_todb(conf_data)
                self.logger.info(f"Number of Top Conferences added: {i+1} ")
            except Exception as e:
                self.logger.error(
                    f"Error while parsing page {link}, find full trace {e}")
        for i, link in enumerate(all_conference_links):
            try:
                conf_data = self._parse_all_conference(link=link)
                if not conf_data:
                    pass
                else:
                    self.push_todb(conf_data)
                self.logger.info(f"Number of All Conferences added: {i+1}")
            except Exception as e:
                self.logger.error(
                    f"Error while parsing {link}, full trace {e}"
                )

    def _get_conferences_list(self, which: str) -> List[str]:
        """
        parses topconferences baseurl and returns -
        - a list of available links
        """
        if which == 'all':
            self._get_all_conf_pages(url=self.all_confs_base_address)
            for link in self.all_conf_page_links:
                content = self.get_page(
                    qlink=link, debug_msg=f"Extracted links from {link}").content
                yield from self._parse_all_conference_base(content=content)
        elif which == 'top':
            content = self.get_page(
                qlink=self.top_conf_address, debug_msg=f"Extracted links from{self.top_conf_address}").content
            yield from self._parse_top_conf_base(content=content)

    # Parsers for top conferences

    def _parse_top_conf_base(self, content: bytes) -> List[str]:
        """
        Wrapper to parse the `/topconf` page and returns
        a list of links for active conferences

        Args:
        content: bytes

        Returns:
        list of conferences: list
        """
        soup = bs(content, "html5lib")
        div_el = soup.find("div", attrs={"id": "ajax_content"})
        conf_tables = div_el.findAll("table")
        for table in conf_tables:
            try:
                anchor = table.h4.a
                if not anchor:
                    pass
                else:
                    link = f"http://www.guide2research.com{anchor['href']}"
                    yield link
            except Exception as e:
                PageParsingError(
                    f"The following error occured while trying to parse an anchor element {e}")
        self.logger.debug('Successfully scraped links of all top conferences')

    def _parse_top_conference(self, link: str) -> Conference:
        """
        Parses individual top conference page and,
        return Conference object

        Args:
        ---
        link: str

        Returns:
        ---
        Conference: object
        """
        page = self.get_page(qlink=link, debug_msg=f'Parsing {link}',
                             allow_redirects=True)
        try:
            content = page.content
        except Exception as e:
            PageParsingError(
                f"The following error occured while parsing {link} Trace:{e}")
        soup = bs(content, "html5lib")
        post_div = soup.find("div", attrs={"class": "single_post"})
        post_tables = post_div.find_all("table")
        title = soup.h1.text
        conf_info = self._get_top_conf_info(name=title, table=post_tables[0])
        rating_info = self._get_top_conf_ranking(
            name=title, table=post_tables[1])
        categories = list(rating_info.keys())[1:-1] if rating_info else []
        bulk_text = self._get_top_conf_bulk_text(soup)
        url = conf_info.get("link")
        deadline = conf_info.get("deadline")
        metadata = Metadata(__name__,
                            dt.now(),
                            link,
                            self.base_address,
                            self.scrapper_name,
                            )
        additional_data = {}
        additional_data["dateRange"] = conf_info.get("dateRange")
        additional_data["location"] = conf_info.get("location")
        self.logger.debug(f"{title} is now added to the database")
        if not deadline:
            self.logger.debug(
                f"{title} not added, because, deadline info not available")
            return None
        else:
            return Conference(title=title,
                              url=url,
                              deadline=deadline,
                              metadata=metadata,
                              bulkText = bulk_text,
                              categories=categories ,
                              rankings=rating_info,
                              **additional_data)

    def _get_top_conf_info(self, name: str, table: bs) -> Dict[str, object]:
        """
        Parses conference info table and
        returns information dictionary

        Args:
        ---
        table: bs4 table

        Returns:
        ---
        conference information dictionary
        """
        try:
            tds = table.findAll("td")
            deadline_string = " ".join(tds[1].text.split()[1:])
            if deadline_string != "be confirmed":
                deadline = self.get_date(deadline_string, fmt="%d %b %Y")
            else:
                deadline = None
            dateRange = [self.get_date(string=date)
                         for date in tds[4].text.strip().split("-")]
            location = tds[6].text.strip()
            link = tds[8].text.strip()
            self.logger.debug(f'Generated conference info for {name}')
            return ({"deadline": deadline,
                     "dateRange": dateRange,
                     "location": location,
                     "link": link})
        except Exception as e:
            self.logger.error(
                f"Error generating conference information for top conference {e}")

    def _get_top_conf_ranking(self, name: str, table: bs) -> Dict["str", "str"]:
        """
        Parses conference ranking info table andBeautifulSoup
        returns ranking information dictionary

        Args:
        ---
        table: bs4 table

        Returns:
        ---
        conference ranking information dictionary
        """
        try:
            tds = table.findAll("td")
            hindex = tds[-1].b.text
            keys = []
            values = []
            for i, td in enumerate(tds):
                if i != 0 and i!= 3 and i%2 == 1:
                    keys.append(td.text.strip().replace('\n','').replace('\t',''))
                if i != 0 and i!=4 and i%2 == 0:
                    values.append(td.text.strip().replace('\n','').replace('\t',''))
            keys.pop()
            values.pop()
            ranking_dict=dict(zip(keys,values))
            ranking_dict["Google Scholar H5-index"]=hindex
            return ranking_dict
        except Exception as e:
            self.logger.error(
                f"Error occured when generating ranking information for {name}, full error {e}")

    def _get_top_conf_bulk_text(self, soup: bs) -> str:
        """
        Parses page soup and returns bulk text

        Args:
        ---
        soup: bs4 soup

        Returns:
        ---
        bulk text: str
        """
        try:
            paragraphs = soup.find_all("p")
            bulk_text = ""
            for p in paragraphs:
                bulk_text += p.text.strip().replace('\n','')
            return bulk_text
        except Exception as e:
            self.logger.error(f"Error parsing bulk text{e}")

    def _get_all_conf_pages(self, url: str):
        content = self.get_page(qlink=url, debug_msg=f"fetching {url}").content
        soup = bs(content, 'html5lib')
        tables_div = soup.find('div', attrs={'id': 'ajax_content'})
        tables = tables_div.find_all('table')
        spans = tables[-1].find_all('span')
        more = spans[-1]
        if more and more.text == 'More Conferences':
            self.logger.info('Has Next page....')
            nextpage = more.a['href']
            self.logger.debug(
                f"Number of All Conference Pages: {self.all_conf_page_count}")
            self.all_conf_page_count += 1
            self.all_conf_page_links.append(nextpage)
            self.logger.debug(
                f'Added {nextpage} to list of all conference pages')
            self._get_all_conf_pages(url=nextpage)
        else:
            pass

    def _parse_all_conference_base(self, content: bytes) -> List[str]:
        soup = bs(content, "html5lib")
        conference_div = soup.find("div", attrs={"id": "ajax_content"})
        conf_tables = conference_div.findAll(
            "table", attrs={"cellspacing": "0"})
        try:
            for conf in conf_tables:
                details = conf.findAll("td")
                anchor = details[1].h4.a
                if anchor:
                    link = self.base_address + anchor['href']
                    yield(link)
                else:
                    self.logger.error(f'Conference link not found')
            self.logger.debug('Successfully scraped links of all conferences')
        except Exception as e:
            self.logger.error(
                f"Failed to parse links in all conferences page with error {e}")

    def _parse_all_conference(self, link: str):
        """
        Parses individual conference page and,
        return Conference object

        Args:
        ---
        link: str

        Returns:
        ---
        Conference: object
        """
        page = self.get_page(qlink=link, debug_msg=f'Parsing {link}',
                             allow_redirects=True)
        try:
            content = page.content
        except Exception as e:
            self.logger.error(
                f"The following error occured while trying to parse {link} {e}")
        soup = bs(content, "html5lib")
        content_div = soup.find("div", attrs={"id": "content_box"})
        title = content_div.h1.text
        tables = soup.find_all('table')
        conf_info = self._get_all_conf_info(name=title, infotable=tables[0])
        bulk_text = self._get_all_conf_bulk(soup=soup)
        metadata = Metadata(__name__,
                            dt.now(),
                            link,
                            self.base_address,
                            self.scrapper_name,
                            )
        additional_data = {}
        additional_data["bulkText"] = bulk_text
        additional_data["dateRange"] = conf_info.get("dateRange")
        additional_data["location"] = conf_info.get("location")
        deadline = conf_info.get("deadline")
        self.logger.debug(f"{title} is now added to database")
        if not deadline:
            self.logger.debug(
                f"{title} not added because, deadline info not available")
            return None
        else:
            return Conference(title=title,
                              url=conf_info.get("link"),
                              deadline=deadline,
                              metadata=metadata,
                              **additional_data
                              )

    def _get_all_conf_info(self, name: str, infotable: bs) -> Dict[str, object]:
        """
        Parses conference info table and
        returns information dictionary

        Args:
        ---
        table: bs4 table

        Returns:
        ---
        conference information dictionary
        """
        try:
            tds = infotable.findAll('td')
            deadline_string = " ".join(tds[1].text.split()[1:])
            if deadline_string != "be confirmed":
                deadline = self.get_date(deadline_string, fmt="%d %b %Y")
            else:
                deadline = None
            dateRange = [self.get_date(date)
                         for date in tds[4].text.strip().split("-")]
            location = tds[6].text.strip().replace('/n','').replace('\t','')
            link = tds[-1].a["href"]
            self.logger.debug(f'Generated info for {name}')
            return ({"deadline": deadline,
                     "dateRange": dateRange,
                     "location": location,
                     "link": link})
        except Exception as e:
            self.logger.error(
                f"Error {e} occured while parsing Conference information table")

    def _get_all_conf_bulk(self, soup: bs) -> str:
        """
        Parses page soup and returns bulk text

        Args:
        ---
        soup: bs4 soup

        Returns:
        ---
        bulk text: str
        """
        try:
            post = soup.find("div", attrs={"class": "single_post"})
            paragraphs = post.findAll("p")
            bulk_text = ""
            for p in paragraphs:
                bulk_text + p.text.strip().replace('\n','').replace('\t','')
            return bulk_text
        except Exception as e:
            self.logger.error(
                f"Error {e} occured while trying to parse bulk text")
