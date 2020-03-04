import unittest
from datamodels import Metadata
# Scrapper-Service/datamodels

class MetadataTestCase(unittest.TestCase):
    def get_metadata(self):
        worker ="worker"
        date_extracted ="date_extracted"
        website_url = "website_url"
        domain_url = "domain_url"
        domain_name = "domain_name"
        meta_data_obj = Metadata(worker, date_extracted, website_url, domain_url, domain_name)
        return meta_data_obj

    def test_data(self):
        obj = self.get_metadata()
        expected = {'website': 'domain_url', 'domain': 'domain_name', 'website_url': 'website_url', 'date_extracted': 'date_extracted'}
        self.assertEqual(obj.querydata[obj.key], expected)

    def test_query_dict(self):
        obj = self.get_metadata()
        expected ={'metadata.worker': {'website': 'domain_url', 'domain': 'domain_name', 'website_url': 'website_url', 'date_extracted': 'date_extracted'}}
        self.assertDictEqual(obj.querydata, expected)

    def test__str__(self):
        obj = self.get_metadata()
        self.assertEqual(
            "{}".format(obj.querydata), obj.querydata.__str__()
        )

    def test__getitem__(self):
        obj = self.get_metadata()
        expected = "domain_url"
        self.assertEqual(obj.querydata[obj.key]["website"], expected)

if __name__ == '__main__':
    unittest.main()