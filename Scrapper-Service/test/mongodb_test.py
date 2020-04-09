import unittest
import json
import warnings
from datamodels import Conference
from datamodels import Metadata
from database  import mdb
from datetime import datetime
from logging import Logger

class MongoDbTestCase(unittest.TestCase):
#    def __init__(self, methodName):
#        super().__init__(methodName)
    
    def cvt(self,dt):
        dt = dt.split('+')
        time = dt[0]+'Z'
        return datetime.strptime(time,"%Y-%m-%dT%H:%M:%S.%fZ")
    
    def cleanText(self, x):
        del x['bulkText']
        del x['metadata']
        del x['url']
        return x
    
    def cvtDate(self,x):
        x['deadline'] = self.cvt(x['deadline'])  
        x['dateRange'] = [self.cvt(x['dateRange'][0]),
                                self.cvt(x['dateRange'][1])]
        x['finalDue'] = self.cvt(x['finalDue'])
        x['metadata']['plugins']['wikicfp']['dateExtracted'] = self.cvt(x['metadata']['plugins']['wikicfp']['dateExtracted'])
        print()
        x['notificationDue'] = self.cvt(x['notificationDue'])
        return x
    
    def read(self,f_name):
        data = open(f_name,'r')
        json_data = json.loads(data.read())
        id_lst = []
        for x in json_data:
            x = self.cvtDate(x)
            id_lst.append(x)
        return id_lst 
        
    def test_data(self):
        self.assertDictEqual.__self__.maxDiff = None
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            data =  self.read("test_data.json")
#            print(data[0]['metadata']['plugins']['wikicfp']['domain'])
            for i in range(len(data)):
                conf = Conference(title=data[i]['title'], 
                                  url=data[i]['url'],
                                  deadline=data[i]['deadline'], 
                                  metadata= Metadata(data[i]['title'], 
                                                   data[i]['metadata']['plugins']['wikicfp']['dateExtracted'], 
                                                   data[i]['metadata']['plugins']['wikicfp']['websiteUrl'], 
                                                   data[i]['metadata']['plugins']['wikicfp']['website'],
                                                   data[i]['metadata']['plugins']['wikicfp']['domain']
                                                  ),
                                  dateRange = data[i]['dateRange'],
                                  finalDue = data[i]['finalDue'],
                                  location = data[i]['location'],
                                  categories = data[i]['categories'],
                                  bulkText = data[i]['bulkText']
                                ) 
            
                count =  mdb.MongoDatabase(Logger,"Conference_Notify","conferences").put(conf)
                self.assertEqual(i+1,count)
           
if __name__ == '__main__':
    unittest.main()
    
#Before Commenting(Loggers):
#    
#
#After Commenting(loggers)
#
#C:\Users\Lenovo\Desktop\open_src_notify\Conference-Notify\Scrapper-Service>python -m unittest mongodb_test
#
#
#
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.049s

#OK