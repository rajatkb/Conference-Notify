import logging
from datetime import datetime as dt
from typing import Dict, List

import requests
from bs4 import BeautifulSoup as bs

from commons import PageParsingError, Scrapper
from datamodels import Conference, Metadata
class Guide2ResearchScrapper(Scrapper):
    def __init__(self, **config):
        super().__init__(context_name=__name__, **config)
        self.base_address = "http://www.guide2research.com/"
        self.top_conf_address = self.base_address + "topconf/"
        self.all_conf_address = self.base_address + "conferences/"
        self.site_name = "guide2research"

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
        n_top_confs = len(top_conference_links)
        n_all_confs = len(all_conference_links)
        for i,link in enumerate(top_conference_links):
            try:
                conf_data = self._parse_top_conference(link=link)
                self.logger.info(f"Conference {i}/{n_top_confs} Top Conferences added")
                self.push_todb(conf_data)
            except Exception as e:
                self.logger.error(
                    f"Error while parsing page {link}, find full trace {e}")
        for i,link in enumerate(all_conference_links):
            try:
                conf_data = self._parse_all_conference(link=link)
                self.logger.info(f"Conference {i}/{n_all_confs} All Conferences added")
                self.push_todb(conf_data)
            except Exception as e:
                self.logger.error(
                    f"Error while parsing {link}, full trace {e}"
                )

    def _get_page(self, base_address: str) -> bytes:
        """
        Takes in page address and returns html content

        Args:
        ---
        base_address: string

        Returns:
        ---
        page content: bytes

        """
        page = requests.get(base_address)
        if not page.status_code == 200:
            self.logger.error(f"loading {base_address} failed with {page.status_code}")
        try:
            return page.content
        except Exception as e:
            PageParsingError(
                f"The following error occured when trying to parse a page {e}")

    def _get_conferences_list(self, which: str) -> List[str]:
        """
        parses topconferences baseurl and returns -
        - a list of available links
        """
        if which == 'all':
            content = self._get_page(base_address=self.all_conf_address)
            return self._parse_all_conference_base(content=content)
        elif which == 'top':
            content = self._get_page(base_address=self.top_conf_address)
            return self._parse_top_conf_base(content)

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
        links = []
        for table in conf_tables:
            try:
                anchor = table.h4.a
                if not anchor:
                    pass
                else:
                    link = f"http://www.guide2research.com{anchor['href']}"
                    links.append(link)
            except Exception as e:
                PageParsingError(
                    f"The following error occured while trying to parse an anchor element {e}")
        return links

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
        page = requests.get(link, allow_redirects=True)
        if not page.status_code == 200:
            self.logger.error(f"loading {link} failed with {page.status_code}")
        try:
            content = page.content
        except Exception as e:
            PageParsingError(
                f"The following error occured while parsing {link} Trace:{e}")
        soup = bs(content, "html5lib")
        post_div = soup.find("div", attrs={"class": "single_post"})
        post_tables = post_div.find_all("table")
        title = soup.h1.text
        conf_info = self._get_top_conf_info(table=post_tables[0])
        rating_info = self._get_top_conf_ranking(name=title, table=post_tables[1])
        bulk_text = self._get_top_conf_bulk_text(soup)
        url = conf_info.get("link")
        deadline = conf_info.get("deadline")
        metadata = Metadata(__name__,
                            dt.now(),
                            link,
                            self.base_address,
                            'Guide2Research',
                            )
        additional_data = {}
        additional_data["dates"] = conf_info.get("dates")
        additional_data["rankings"] = rating_info
        additional_data["address"] = conf_info.get("address")
        additional_data["bulkText"] = bulk_text
        self.logger.info(f"{title} is now added to the database")
        return Conference(title=title,
                          url=url,
                          deadline=deadline,
                          metadata=metadata,
                          **additional_data)

    def _get_top_conf_info(self, table: bs) -> Dict[str, object]:
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
            deadline = tds[1].text.strip()
            dates = tds[4].text.strip().split("-")
            address = tds[6].text.strip()
            link = tds[8].text.strip()
            return ({"deadline": deadline,
                     "dates": dates,
                     "address": address,
                     "link": link})
        except Exception as e:
            self.logger.error(
                f"Error generating conference information for top conference {e}")

    def _get_top_conf_ranking(self, name:str, table: bs) -> Dict["str", "str"]:
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
            g2rranking = tds[2].text
            category_a = tds[5].text.strip()
            category_a_value = tds[6].text.strip()
            category_b = tds[7].text.strip()
            category_b_value = tds[8].text.strip()
            category_c = tds[9].text.strip()
            category_c_value = tds[10].text.strip()
            hindex = tds[-1].font.text
            self.logger.info(f"Generated ranking info for {name}")
            return ({"Guide2Research Overall Ranking": g2rranking,
                     category_a: category_a_value,
                     category_b: category_b_value,
                     category_c: category_c_value,
                     "g_scholar_h5_index": hindex})
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
                bulk_text+= p.text.strip()
            return bulk_text
        except Exception as e:
            self.logger.error(f"Error parsing bulk text{e}")

    def _parse_all_conference_base(self, content: bytes) -> List[str]:
        soup = bs(content, "html5lib")
        conference_div = soup.find("div", attrs={"id": "ajax_content"})
        conf_tables = conference_div.findAll("table", attrs={"cellspacing": "0"})
        links = []
        try:
            for conf in conf_tables:
                details = conf.findAll("td")
                anchor = details[1].h4.a
                if anchor:
                    link = self.base_address + anchor['href']
                    links.append(link)
                else:
                    self.logger.error(f'Conference link not found')
            return links
        except Exception as e:
            self.logger.error(f"Failed to parse links in all conferences page with error {e}")

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
        self.logger.info(f'Parsing {link}')
        page = requests.get(link, allow_redirects=True)
        if not page.status_code == 200:
            self.logger.error(f"loading {link} failed with {page.status_code}")
        try:
            content = page.content
        except Exception as e:
            self.logger.error(
                f"The following error occured while trying to parse {link} {e}")
        soup = bs(content, "html5lib")
        content_div = soup.find("div", attrs={"id": "content_box"})
        title = content_div.h1.text
        tables = soup.find_all('table')
        conf_info = self._get_all_conf_info(infotable=tables[0])
        bulk_text = self._get_all_conf_bulk(soup=soup)
        metadata = Metadata(__name__,
                            dt.now(),
                            link,
                            self.base_address,
                            'Guide2Research',
                            )
        additional_data = {}
        additional_data["bulkText"] = bulk_text
        additional_data["dates"] = conf_info.get("dates")
        additional_data["address"] = conf_info.get("address")
        self.logger.info(f"{title} is now added to database")
        return Conference(title=title,
                          url=conf_info.get("link"),
                          deadline=conf_info.get("deadline"),
                          metadata=metadata,
                          **additional_data
                          )

    def _get_all_conf_info(self, infotable: bs) -> Dict[str, object]:
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
            deadline = tds[1].text.strip()
            dates = tds[4].text.strip().split("-")
            address = tds[6].text.strip()
            link = tds[-1].a["href"]
            return ({"deadline": deadline,
                     "dates": dates,
                     "address": address,
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
                bulk_text + p.text.strip()
            return bulk_text
        except Exception as e:
            self.logger.error(
                f"Error {e} occured while trying to parse bulk text")