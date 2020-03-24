import unittest
from datamodels import Metadata
from datetime import datetime
# Scrapper-Service/datamodels

class MetadataTestCase(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
    
    def get_valid_data(self):
        return Metadata(__name__, datetime.now(), "something.com/something", "something.com","anythingProd" )

    def get_invalid_data(self):
        return Metadata(__name__, "anything", "something.com/something", "something.com","anythingProd" )        


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
            self.assertEqual(success , True , "Metadata taking in bad datetime value, can pass string in it")



if __name__ == '__main__':
    unittest.main()