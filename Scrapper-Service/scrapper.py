import requests
import logging
from bs4 import BeautifulSoup
from collections import deque





class Conference:
    def __init__(self, **kwargs):
        """ [Conference class]
            Used for modeling the data of conferences
        """
        self.title = kwargs['title']
        self.url = kwargs['url']
        self.date_range = kwargs['date_range']
        self.location = kwargs['location']
        self.submission_deadline = kwargs['deadline']
        self.notification_due = kwargs['notificationdue']
        self.final_version_due = kwargs['finaldue']
        self.categories = kwargs['categories']
        self.bulk_text = kwargs['bulk_text']
        self.dict_data = kwargs

    def __str__(self):
        return str(self.dict_data)

class Scrapper:
    def __init__(self , log_level):
        logger = logging.getLogger(__name__)
        logger.setLevel(log_level)
        log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_stream =logging.StreamHandler()
        log_stream.setFormatter(log_format)
        logger.addHandler(log_stream)
        self.logger = logger

    def run(self):
        """ [run function]
            to be called by the main.py and is not to be
            extended or reimplemented. Run contains necessary runtime
            methods for making sure the the user implemented method gets called
        """
        pass

    def get_conferences(self):
        """ [get_conference]
            TO BE IMPLEMENTED BY THE USER
            The function is intended to return a iterator
            of the objects of Conference()
            
        Returns:
            [Iterator[Conference]] --   Returns iterator of conference information
                                        After parsing the conference page as intented by the user
        """
        return iter([])


class WikiCfpScrapper(Scrapper):

    def __init__(self , log_level):
        self.base_address = "http://www.wikicfp.com"
        self.site_name = "wikicfp"
        super().__init__(log_level)
    
    def catgory_list(self , base_address:str , site_name:str ):  
        req = requests.get("{}/cfp/allcat?sortby=1".format(base_address)) # getting page listed in specific order
        if 200 <= req.status_code <=299:
            self.logger.debug("{} category page extracted".format(site_name))
        else:
            raise requests.HTTPError

        page_dom = BeautifulSoup(req.content , 'html.parser')
        table_container = page_dom.find(attrs={"class":"contsec"}) ## table in the page
        if table_container is None:
            self.logger.error("{} no element contsec at category page".format(site_name))
            raise Exception("{} no element contsec at category page".format(site_name))
        
        anchors = table_container.select("tr td a")
        if len(anchors) == 0:
            self.logger.error("{} no anchor found".format(site_name))
            raise Exception("{} no anchor found".format(site_name))
        
        anchors = anchors[1:]    
        links = map(lambda anchor: (anchor.text, anchor["href"])  , anchors)
        return links

    def next_anchor(self , base_address:str , category:str ,  link:str):
        req = requests.get(base_address+link)
        if 200 <= req.status_code <=299:
            self.logger.debug("{} page extracted".format(category))
        else:
            raise requests.HTTPError
        page_dom = BeautifulSoup(req.content , 'html.parser')
        page_dom = page_dom.find(attrs={"class":"contsec"})
        page_dom = page_dom.find(name = "center")
        
        table_container = page_dom.find(name = "form" , attrs={"name":"myform"} , recursive= False)
        table_container = table_container.find(name = "table" , recursive = False)
        if table_container is None:
            self.logger.error("{} no element form ".format(category))
            raise Exception("{} no element form ".format(category))
        trs = table_container.find_all("tr" , recursive = False)
        tr = trs[-1]
        content = trs[-2]
        anchors = tr.find_all("a")
        anchor = list(filter(lambda x: x.text == "next"  ,anchors))[0]
        return (content,anchor)

    def iterate_pages(self, base_address:str , category:str , link:str):
        curr_table_container , next_a = self.next_anchor(base_address , category , link)
        self.logger.debug("{} category link \" {} \" extracted ".format(category , link))
        yield curr_table_container
        prev_link = link
        link = next_a["href"]
        while True:
            curr_table_container , next_a= self.next_anchor(base_address , category , link) 
            self.logger.debug("{} category link \" {} \" extracted ".format(category , link))
            yield curr_table_container
            link = next_a["href"]
            if prev_link == link and prev_link is not None:
                break
            prev_link = link

    def iterate_categories(self , base_address:str , site_name:str):
        for (category , link) in self.catgory_list(base_address , site_name):
            try: 
                yield from self.iterate_pages(base_address , category , link)
            except Exception:
                self.logger.error("Failed to extract complete data from {} starting at {}".format(category , link))

    def iterate_links(self , base_address:str , site_name:str):
        for parsed_pages in self.iterate_categories(base_address , site_name):
            links = parsed_pages.select("a")
            links = map(lambda x: (x.text , x["href"]) , links)
            for link in links:
                yield link


    def extract_info(self , page_dom):
        info_table = page_dom.select("table.gglu")
        list_info_title = map(lambda x: x.text.strip() ,  info_table[0].select("th"))
        list_info_content = map(lambda x:x.text.strip() , info_table[0].select("td"))
        info = {"date_range":"" , "location":"" , "deadline":"" , "notificationdue":"" , "finaldue":""}
        for title , content in zip(list_info_title , list_info_content):
            if title == "When":
                info["date_range"] = content
            elif title == "Where":
                info["location"] = content
            elif title == "Submission Deadline":
                info["deadline"] = content
            elif title == "Notification Due":
                info["notificationdue"] = content
            elif title == "Final Version Due":
                info["finaldue"] = content
        return info

    def extract_categories(self , page_dom):
        anchor_list = page_dom.select("table.gglu tr td a")
        anchor_list = map(lambda x: x.text , anchor_list[1:])
        return list(anchor_list)

    def parse_conference_page_info(self , page:str):
        page_dom = BeautifulSoup(page , 'html.parser')
        title = page_dom.find(name = "span" , attrs={"property":"v:description"}).text
        url = page_dom.find(name = "a" , attrs={"target":"_newtab"})["href"]
        info = self.extract_info(page_dom)
        categories = self.extract_categories(page_dom)
        bulk_text = page_dom.select("div.cfp")[0].text
        print(title.text, url["href"], info , categories , bulk_text)
        return Conference(**info , **{"title":title , "url":url , "categories":categories , "bulk_text":bulk_text })

    def get_conferences(self):
        base_address = self.base_address 
        site_name = self.site_name
        linkSet = set()
        for name , link in self.iterate_links(base_address , site_name):
            if hash(link) in linkSet:
                continue
            linkSet.add(hash(link))
            req = requests.get(base_address + link)
            if 200 <= req.status_code <=299:
                self.logger.debug("Page extracted for conference {} link: {}  extracted".format(name , link))
            else:
                raise requests.HTTPError
            try:
                conference_data = self.parse_conference_page_info(req.content)
                yield conference_data
            except Exception:
                self.logger.error("Error when parsing link {}".format(link))





WikiCfpScrapper(logging.DEBUG).run()
