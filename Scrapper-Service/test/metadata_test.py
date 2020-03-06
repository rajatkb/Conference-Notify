import unittest
from datamodels import Metadata
# Scrapper-Service/datamodels

class MetadataTestCase(unittest.TestCase):
    def get_metadata(self):
        worker ="worker"
        date_extracted ="dateExtracted"
        website_url = "websiteUrl"
        domain_url = "domainUrl"
        domain_name = "domainName"
        meta_data_obj = Metadata(worker, date_extracted, website_url, domain_url, domain_name)
        return meta_data_obj

    def test_data(self):
        obj = self.get_metadata()
        expected = {'website': 'domainUrl', 'domain': 'domainName', 'websiteUrl': 'websiteUrl', 'dateExtracted': 'dateExtracted'}
        self.assertEqual(obj.querydata[obj.key], expected)

    def test_query_dict(self):
        obj = self.get_metadata()
        expected ={'metadata.worker': {'website': 'domainUrl', 'domain': 'domainName', 'websiteUrl': 'websiteUrl', 'dateExtracted': 'dateExtracted'}}
        self.assertDictEqual(obj.querydata, expected)

    def test__str__(self):
        obj = self.get_metadata()
        self.assertEqual(
            "{}".format(obj.querydata), obj.querydata.__str__()
        )

    def test__getitem__(self):
        obj = self.get_metadata()
        expected = "domainUrl"
        self.assertEqual(obj.querydata[obj.key]["website"], expected)

    def test_querydata_type(self):
        obj = self.get_metadata()
        expected = "dict"
        self.assertEqual(type(obj.querydata).__name__, expected)

    def test_worker_type(self):
        obj = self.get_metadata()
        res =type(obj.worker).__name__
        expected = "str"
        self.assertEqual(res, expected)

    def test_key_type(self):
        obj = self.get_metadata()
        res = type(obj.key).__name__
        expected = "str"
        self.assertEqual(res, expected)

    def test_dateExtracted_type(self):
        obj = self.get_metadata()
        res = type(obj.querydata[obj.key]["dateExtracted"]).__name__
        expected = "datetime"
        self.assertEqual(res, expected)

    def test_websiteUrl_type(self):
        obj = self.get_metadata()
        res = type(obj.querydata[obj.key]["websiteUrl"]).__name__
        expected = "str"
        self.assertEqual(res, expected)
        
    def test_website_type(self):
        obj = self.get_metadata()
        res = type(obj.querydata[obj.key]["website"]).__name__
        expected = "str"
        self.assertEqual(res, expected)

    def test_domain_type(self):
        obj = self.get_metadata()
        res = type(obj.querydata[obj.key]["domain"]).__name__
        expected = "str"
        self.assertEqual(res, expected)
        
        

if __name__ == '__main__':
    unittest.main()