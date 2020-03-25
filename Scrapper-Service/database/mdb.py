from pymongo import MongoClient
import pymongo
import logging
from logging import Logger
from datamodels import Conference, Metadata
from commons import Database

class MongoDatabase(Database):
    
    def __init__(   self  , logger:Logger ,  database_name:str , collection_name:str , 
                    host:str ='localhost' , port:int=27017 , maxPoolSize:int = None , **kwargs):
        """Mongo database object
        Arguments:
            logger {[logging]} -- logger passed by user 
            database_name {[type]} -- name of database to be used
            collection_name {[type]} -- collection for the mongodb db
        
        Keyword Arguments:
            host {str} -- host for mongodb (default: {'localhost'})
            port {int} -- port for mongodb (default: {27017})
            maxPoolSize {[type]} -- maxpoolsize for mongo db (default: {None})
        
        Raises:
            e:  error when database connection fails. These are unhandled connection 
                and the application must stop immeditely in such cases
        """
        self.logger = logger
        try:
            self.logger.debug("Using Database name {}".format(database_name))
            self.logger.debug("Using address {}:{}".format(host , port))    
            client =  MongoClient(host , int(port) , maxPoolSize = maxPoolSize)
            self.client = client
            db = client[database_name] ## Create a new database if not existing
            ##
            ## Quirks of pymongo client , any error from this statement below
            ## leads to unsuported operation for database , where as intended
            ## strcuture is a collection. Should be addressed in the pymongo
            self.logger.debug("Using Collection name {}".format("conferences"))
            collection = db[collection_name]
            client.server_info()
            self.logger.info("Succefully created mongodb client connection on host:{} , port:{} ".format(host , port))
            self.db = db
            self.collection = collection
            index_info = collection.index_information()
            possible_index = Conference.index() #  -> [(string,bool)]
            possible_index = filter(lambda x: (x[0]+"_1") not in index_info , possible_index)
            for idx , unique in possible_index:
                collection.create_index([(idx , pymongo.ASCENDING )] , unique = unique )
                
        except Exception as e:
            self.logger.error("Failed to initiate mongodb client error: {}".format(e))
            raise e
    

    def __del__(self):
        self.logger.info("Closing connection to mongodb !!")
        self.client.close()
        self.logger.info("Succesfully Closed connection to mongodb !!")

    def put(self , conference_data):
        if not isinstance(conference_data , Conference):
            raise ValueError("Provided data is not in proper format as required by db")
        else:
            _id = conference_data._id
            try:
                if(self.collection.find({'_id':_id}).count()==0):
                    res = self.collection.update_one( {'_id':_id,'deadline':{'$gte':conference_data.querydata['deadline']}}  ,conference_data.get_query(), upsert = True)
                    self.logger.debug("""   Value inserted message matched count: {} modified count: {} upserted id: {}"""
                                      .format(res.matched_count , res.modified_count , res.upserted_id))
            except Exception as e:
                self.logger.error("Failed to commit data error : {}".format(e))