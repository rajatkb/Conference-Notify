import unittest
from database import mdb
from datamodels import Conference
from datamodels import Metadata
from datetime import datetime
from logging import Logger

class MongoDbTestCase(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
    
    def get_valid_data(self):
        conference = Conference(title="something", 
                            url="anything", deadline=datetime.now(), dateRange=[datetime.now(),datetime.now()],
                            metadata=Metadata(__name__, datetime.now(), "something.com/something", "something.com","anythingProd" ))
        mdb.MongoDatabase(logger=Logger,database_name="Conference_Notify" , collection_name="conferences").put(conference)
        print("Test Run sucessfully")

    def get_invalid_data(self):
        conference = Conference(title="something", 
                            url="anything", deadline="anything", 
                            metadata="anything")
        
        mdb.MongoDatabase(logger=Logger,database_name="any_database" , collection_name="any_collection").put(conference)
        print("Test fail sucessfully")

    def test_valid_data(self):
        self.get_valid_data()
    
    def test_invalid_data(self):
        success = True
        try:
            self.get_invalid_data()
            success = False
        except Exception as e:
            print("Object initialisation failed successfully ",e)
        finally:
            self.assertEqual(success , True , "Database configurations are not correct ")



if __name__ == '__main__':
    unittest.main()