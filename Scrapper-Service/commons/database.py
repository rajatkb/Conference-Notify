from abc import ABC , abstractclassmethod , abstractmethod , abstractproperty
import logging
from logging import Logger

class Database:
    
    @abstractclassmethod
    def __init__(   self  , logger:Logger ,  database_name:str , collection_name:str  , 
                    host:str ='localhost' , port:int=27017 , maxPoolSize:int = None , **kwargs):
                    """ Database interface
                        Arguments:
                            logger {[logging]} -- logger passed by user 
                            database_name {[type]} -- name of database to be used
                            collection_name {[type]} -- collection / table name for the db
                        
                        Keyword Arguments:
                            host {str} -- host for db (default: {'localhost'})
                            port {int} -- port for db (default: {27017})
                            maxPoolSize {[type]} -- maxpoolsize for db (default: {None})
                        
                        Raises:
                            e:  error when database connection fails. These are unhandled connection 
                                and the application must stop immeditely in such cases
                        """
                    
                    
                    pass
    
    @abstractclassmethod
    def __del__(self):
        pass

    @abstractclassmethod
    def put(self , conference_data):
        pass