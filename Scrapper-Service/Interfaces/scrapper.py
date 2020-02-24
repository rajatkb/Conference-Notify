import logging
import datetime
from Database import Database
from DataModels import Metadata
from abc import *


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




    def __init__(self , log_level , context_name  , **config):
        logger = logging.getLogger(context_name)
        logger.setLevel(log_level)
        log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_stream =logging.StreamHandler()
        log_stream.setFormatter(log_format)
        logger.addHandler(log_stream)
        self.logger = logger     
        self.db = Database(logger, **config)
        self.logger.info("{} setup complete !!".format(__name__))

    class PageParsingError(ValueError):
        """[Raised when parsing fails]
        """
        pass

    def run(self):
        """ [run function]
            to be called by the main.py and is not to be
            extended or reimplemented. Run contains necessary runtime
            methods for making sure the the user implemented method gets called
        """
        self.logger.info("Scrapper started !! Inserting data into db")
        self.parse_action(self.db.put)
        self.logger.info("Scrapper done , all information available in db")


    @abstractmethod
    def parse_action(self , dbaction):
        """[parse_action]
            TO BE IMPLEMENTED BY THE USER
            The function is intended to return a iterator
            of the objects of Conference()
            the dbaction passes in the database push function , so that
            implementor can decide for themselves. One can also implement this method 
            using Ayncio / Thread / MultiProcessing
        
        Arguments:
            dbaction {[function( Confernece )]} --  Action passed by run , should be called for making updates
                                                    Pass Conference object as an argumenet

        """