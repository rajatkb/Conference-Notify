import requests
import logging
from bs4 import BeautifulSoup
from Interfaces import Scrapper
from DataModels import Conference , Metadata
import datetime

# Once you are done implementing below 
# you can move to config.json and change settings like this
# ........
# .............
# 
# "load":[
#       {     "filename":"Scrappers.wikicfp",
#             "class":"WikiCfpScrapper"
#       },
#       {
#             "filename":"Scrappers.demo",
#             "class":"DemoScrapper"
#       } 
#          .....
#   ]


class DemoScrapper(Scrapper):
    
    def __init__(self , **config):
        """Demo scrapper to demonstrate how to create Scrapper
        
        Arguments:
            **config : holds configuration to be passed to super
        """
        super().__init__(context_name =__name__ , **config)
        self.logger.info("Demo initialized !!!")
        pass
        ## Initialize

    def parse_action(self , dbaction):

        meta = Metadata(__name__ , datetime.datetime.now() , 
                        website_url="somename.co.in/link" , 
                        domain_url="somename.co.in" , 
                        domain_name="somename" , **{ "extra":"info you want to keep"} )

        data = Conference(**{  "title": "" , "url": "" , 
                                "categories": "" , "bulk_text": ""  , "metadata":meta}) 
        
        ## There are other optional fields also for conference
        ## check out the docstring
        ## Once done you can call dbaction


        # dbaction(data)
        self.logger.info("Yay !! data was put into db hopefully !! Check error logs , i.e run with log level error")
        # Remember this function will only be called once by the 
        # run method of parent class so implement your loop inside here 
        # and call the dbaction to put the data.
        
