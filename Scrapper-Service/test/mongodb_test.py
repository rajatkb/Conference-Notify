import unittest
import pymongo as pym
import json
import warnings
from datetime import datetime

class ReadData():
    def __init__(self,f_name):
        self.f_name=f_name
        self.json_data = None
    def cvt(self,dt):
        dt = dt.split('.')[0]
        dt = dt.replace('T',' ')
        dt = datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
        return dt
    def cleanText(self, x):
        del x['bulkText']
#        del x['metadata']
#        del x['url']
        return x
    def cvtDate(self,x):
        x['deadline'] = self.cvt(x['deadline'])  
        x['dateRange'] = [self.cvt(x['dateRange'][0]),
                                self.cvt(x['dateRange'][1])]
        x['finalDue'] = self.cvt(x['finalDue'])
        x['metadata']['plugins']['wikicfp']['dateExtracted'] = self.cvt(x['metadata']['plugins']['wikicfp']['dateExtracted'])
        x['notificationDue'] = self.cvt(x['notificationDue'])
        return x
    
    def read(self):
        data = open(self.f_name,'r')
        json_data = json.loads(data.read())
        id_lst = []
        for x in json_data:
            x = self.cvtDate(x)
            id_lst.append(x)
        return id_lst    

class MongoDbTestCase(unittest.TestCase):
    def test_data(self):
        self.assertDictEqual.__self__.maxDiff = None
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            myclient = pym.MongoClient("mongodb://localhost:27017/")
            mydb = myclient['Conference_Notify']
            collection = mydb['conferences']
            rds = ReadData('test_data.json')
            data = rds.read()
            for x in data:
                mongo_data = collection.find_one({"_id":x['_id']})
                x = rds.cleanText(x)
                mongo_data= rds.cleanText(mongo_data)
#                print(x['dateRange'])
#                print(mongo_data['dateRange'])
                self.assertDictEqual(x,mongo_data)
                print("test pass")
           
if __name__ == '__main__':
    unittest.main()