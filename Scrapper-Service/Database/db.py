from pymongo import MongoClient
import pymongo
import logging
from DataModels import Conference

class Database:

    class BadDataFormatError(Exception):
        pass    


    def __init__(self  , logger ,  context_name ,  database_name , collection_name  , host='localhost' , port=27017):
        self.logger = logger
        try:
            self.logger.debug("Using Database name {}".format(database_name))
            self.logger.debug("Using address {}:{}".format(host , port))    
            client = MongoClient(host , int(port))
            db = client[database_name] ## Create a new database if not existing
            ##
            ## Quirks of pymongo client , any error from this statement below
            ## leads to unsuported operation for database , where as intended
            ## strcuture is a collection. Should be addressed in the pymongo
            self.logger.debug("Using Collection name {}".format(collection_name))
            collection = db[collection_name]
            sinfo = client.server_info()
            self.logger.debug("Succefully created client connection {}".format(sinfo))
            self.db = db
            self.collection = collection
            modidx = list(map(lambda x: (x, pymongo.ASCENDING ), Conference.index()))
            collection.create_index(modidx)

        except Exception as e:
            self.logger.error("Failed to initiate mongodb client error: {}".format(e))
            raise e
    
    def put(self , conference_data):
        if not isinstance(conference_data , Conference):
            raise self.BadDataFormatError("Provided data is not in proper format as required by db")
        else:
            _id = conference_data._id
            try:
                res = self.collection.update_one( {'_id':_id}  ,{'$set' :conference_data.data()} , upsert = True)
                self.logger.debug("Value inserted message {}".format(res))
            except Exception as e:
                self.logger.error("Failed to commit data error : {}".format(e))