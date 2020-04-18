import requests
import logging
from bs4 import BeautifulSoup
from commons import Scrapper
from datamodels import Conference , Metadata
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

    def __del__(self):
        self.logger.info("{} done scrapping !!!".format(__name__))

    def parse_action(self):

        meta = Metadata(__name__ , datetime.datetime.now() , 
                        website_url="somename.co.in/link" , 
                        domain_url="somename.co.in" , 
                        domain_name="somename" , **{ "extra":"info you want to keep"} )

        data = Conference(**{  "title": "" , "url": "" , 
                               "deadline":datetime.datetime.now() , "metadata":meta}) 
        
        ## There are other optional fields also for conference
        ## check out the docstring
        ## Once done you can call dbaction

        ## Use the already provided method from Scrapper class like
        ## getDate , getPage etc.
        ## They are tested methods and have lesser chance of breaking your code.

        # self.getPage(" -- some page link --" , " -- some debug message --") 
        # 
        # PARSE DATA 
        # 
        # self.push_todb(data)

        
        self.logger.info("Yay !! data was put into db hopefully !! Check error logs , i.e run with log level error")
        # Remember this function will only be called once by the 
        # run method of parent class so implement your loop inside here 
        # and call the dbaction to put the data.
        
