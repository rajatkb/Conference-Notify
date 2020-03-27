import logging
import datetime
from utility import get_logger , print_start , AdaptiveRequest
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




    def __init__(self , context_name , log_level , log_stream , log_folder , database_module , db_configuration ,   **kwargs):
        self.logger = get_logger(context_name , log_level , log_stream , log_folder)  
        print_start(self.logger)   
        self.db = database_module(self.logger , **db_configuration)
        self.logger.info("{} setup complete !!".format(context_name))
        self.arequest = AdaptiveRequest()

        if self.db != None:
            self.push_todb = self.db.put
        else:
            raise ValueError("No database parameter given")

    def get_page(self, qlink , debug_msg = "failed to extract page", **kwargs):
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
        req = self.arequest.get(qlink, **kwargs)
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
    def parse_action(cls):
        """[parse_action]
            TO BE IMPLEMENTED BY THE USER
            The function is intended to return a iterator
            of the objects of Conference()
            the dbaction passes in the database push function , so that
            implementor can decide for themselves. One can also implement this method 
            using Ayncio / Thread / MultiProcessing

        """