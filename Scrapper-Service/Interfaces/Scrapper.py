import logging
import datetime
from Database import Database
from abc import ABC , abstractmethod


class Scrapper(ABC):

    def get_date(self , string):
        string = string.strip()
        try:
            return datetime.datetime.strptime(string , "%b %d, %Y")
        except Exception as e:
            self.logger.error("Bad string format error : {}".format(e))
            return string

    def __init__(self , log_level , context_name  , **config):
        logger = logging.getLogger(context_name)
        logger.setLevel(log_level)
        log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_stream =logging.StreamHandler()
        log_stream.setFormatter(log_format)
        logger.addHandler(log_stream)
        self.logger = logger     
        self.db = Database(logger , context_name, **config)

    class PageParsingError(Exception):
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
        for conf in self.get_conferences():
            self.db.put(conf)
            
        self.logger.info("Scrapper done , all information available in db")

    @abstractmethod
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