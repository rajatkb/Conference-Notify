import logging
import datetime
from utility import getLogger , printStart
from datamodels import Conference, Metadata
from abc import ABC , abstractclassmethod , abstractmethod , abstractproperty
import requests

class Scrapper(ABC):

    def get_date(self , string , fmt = "%b %d, %Y" ):
        """ Utility for converting date given string
            amd format of date time
        Arguments:
            string {[str]} -- date in string
        
        Keyword Arguments:
            fmt {str} -- formatter for date (default: {"%b %d, %Y"})
        
        Returns:
            [datetime] -- time in datetime object format 
        """
        string = string.strip()
        try:
            return datetime.datetime.strptime(string , fmt )
        except Exception as e:
            self.logger.warn("Bad string format error : {}".format(e))
            return string


    def __init__(self , context_name , log_level , log_stream  , getDatabaseObject = lambda logger: None ,  **kwargs):
        self.logger = getLogger(context_name , log_level , log_stream)  
        printStart(self.logger)   
        self.db = getDatabaseObject(self.logger)
        self.logger.info("{} setup complete !!".format(context_name))
        if self.db != None:
            self.push_todb = self.db.put
        else:
            raise ValueError("No database parameter given")

    def getPage(self, qlink , debug_msg = "failed to extract page"):
        """[summary]
        
        Arguments:
            qlink {[str]} -- link to request
        
        Keyword Arguments:
            debug_msg {str} -- debug log message for failing (default: {"failed to extract page"})
        
        Raises:
            requests.HTTPError: if page not found
            requests.Timeout: if no reponse from server , default is 1sec
        Returns:
            [request] -- request page
        """
        req = requests.get(qlink , timeout = 1)
        if 200 <= req.status_code <=299:
            self.logger.debug(debug_msg)
        else:
            raise requests.HTTPError
        return req


    def run(self):
        """ [run function]
            to be called by the main.py and is not to be
            extended or reimplemented. Run contains necessary runtime
            methods for making sure the the user implemented method gets called
        """
        self.logger.info("Scrapper routine started !!")
        self.parse_action()
        self.logger.info("Scrapper routine done !!")


    @abstractclassmethod
    def parse_action(self):
        """[parse_action]
            TO BE IMPLEMENTED BY THE USER
            The function is intended to return a iterator
            of the objects of Conference()
            the dbaction passes in the database push function , so that
            implementor can decide for themselves. One can also implement this method 
            using Ayncio / Thread / MultiProcessing

        """