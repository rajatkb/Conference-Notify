from pymongo import MongoClient
import pymongo
import logging
from DataModels import Conference, Metadata

class Database:
   
    def __init__(self  , logger ,  database_name , collection_name  , host='localhost' , port=27017 , maxPoolSize = None , **kwargs):
        """[summary]
        
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
            client = MongoClient(host , int(port) , maxPoolSize = maxPoolSize)
            self.client = client
            db = client[database_name] ## Create a new database if not existing
            ##
            ## Quirks of pymongo client , any error from this statement below
            ## leads to unsuported operation for database , where as intended
            ## strcuture is a collection. Should be addressed in the pymongo
            self.logger.debug("Using Collection name {}".format(collection_name))
            collection = db[collection_name]
            sinfo = client.server_info()
            self.logger.info("Succefully created mongodb client connection on host:{} , port:{} ".format(host , port))
            self.logger.debug("Succefully created client connection {}".format(sinfo))
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
                res = self.collection.update_one( {'_id':_id}  ,{'$set' :conference_data.query_dict()} , upsert = True)
                self.logger.debug("Value inserted message {}".format(res))
            except Exception as e:
                self.logger.error("Failed to commit data error : {}".format(e))