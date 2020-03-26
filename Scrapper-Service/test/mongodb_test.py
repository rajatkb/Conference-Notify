import unittest
from mdb import MongoDatabase
# Scrapper-Service/datamodels

class MongoDbTestCase(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
    
    def get_valid_data(self):
        return MongoDatabase(database_name="Conference_Notify" , collection_name="conferences")

    def get_invalid_data(self):
        return MongoDatabase(database_name="any_database" , collection_name="any_collection")      

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