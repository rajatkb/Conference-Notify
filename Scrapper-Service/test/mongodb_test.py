import unittest
import json
import warnings
from datamodels import Conference
from datamodels import Metadata
from database  import mdb
from datetime import datetime
from datetime import timedelta
from logging import Logger

class MongoDbTestCase(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        self.mongo_db = mdb.MongoDatabase(Logger,"Conference_Notify","conferences")
    
    def test_insert_datetime(self):
        self.assertDictEqual.__self__.maxDiff = None
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            conf = Conference(title="Something", 
                                  url="www.something.com",
                                  deadline=datetime.now(), 
                                  metadata= Metadata("something", 
                                                   datetime.now(), 
                                                   "www.something.com", 
                                                   "www.something.com",
                                                   "something"
                                                  ),
                                  dateRange = [datetime.now(),datetime.now()+timedelta(days=10)],
                                  finalDue = datetime.now(),
                                  location = "something",
                                  categories = ["something"],
                                  bulkText = "somthing"
                                ) 
            
            flag = None
            is_inserted = self.mongo_db.put(conf)
            if(is_inserted !=None):
                flag = True
            else:
                flag = False
                
            self.assertEqual(True,flag)
        
    def test_valid_datetime(self):
        self.assertDictEqual.__self__.maxDiff = None
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            conf = Conference(title="Something", 
                                  url="www.something.com",
                                  deadline=datetime.now()+timedelta(days=10), 
                                  metadata= Metadata("something", 
                                                   datetime.now(), 
                                                   "www.something.com\somthing.html", 
                                                   "www.something.com",
                                                   "something"
                                                  ),
                                  dateRange = [datetime.now(),datetime.now()+timedelta(days=10)],
                                  finalDue = datetime.now(),
                                  location = "something",
                                  categories = ["something"],
                                  bulkText = "somthing"
                                ) 
            
            flag = None
            is_inserted = self.mongo_db.put(conf)
            if(is_inserted !=None):
                flag = True
            else:
                flag = False
                
            self.assertEqual(True,flag)
            
        def test_invalid_datetime(self):
            self.assertDictEqual.__self__.maxDiff = None
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                conf = Conference(title="Something", 
                                  url="www.something.com",
                                  deadline=datetime.now()-timedelta(days=10), 
                                  metadata= Metadata("something", 
                                                     datetime.now(), 
                                                     "www.something.com\somthing.html", 
                                                     "www.something.com",
                                                     "something"
                                                     ),
                                      dateRange = [datetime.now(),datetime.now()-timedelta(days=10)],
                                      finalDue = datetime.now(),
                                      location = "something",
                                      categories = ["something"],
                                      bulkText = "somthing"
                                ) 
                    
                is_inserted = self.mongo_db.put(conf)
                self.assertEqual(None,is_inserted)
            
if __name__ == '__main__':
    unittest.main()
    