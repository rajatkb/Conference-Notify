import logging



class Scrapper:
    
    def __init__(self , log_level):
        logger = logging.getLogger(__name__)
        logger.setLevel(log_level)
        log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_stream =logging.StreamHandler()
        log_stream.setFormatter(log_format)
        logger.addHandler(log_stream)
        self.logger = logger

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
        for conf in self.get_conferences():
            print(conf["title"], conf["url"] , conf["deadline"])

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