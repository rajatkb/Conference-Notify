import unittest
from datamodels import Conference
from datamodels import Metadata

class ConferenceTestCase(unittest.TestCase):
    def get_metadata(self):
        worker ="worker"
        date_extracted ="date_extracted"
        website_url = "website_url"
        domain_url = "domain_url"
        domain_name = "domain_name"
        meta_data_obj = Metadata(worker, date_extracted, website_url, domain_url, domain_name)
        return meta_data_obj

    def get_conferenceobj(self):
        title = "title"
        url = "http://url.com"
        deadline = "deadline"
        metadata = self.get_metadata()
        conference_obj = Conference(title, url, deadline, metadata)
        return conference_obj

    def test_index(self):
        obj = self.get_conferenceobj()
        expected = obj.index()
        self.assertEqual([('url' , False) , ('deadline' , False) , ('title' , False)], expected)

    def test_generate_uuid(self):
        obj = self.get_conferenceobj()
        expected = obj.generate_uuid()
        self.assertEqual('759839e1-5d29-5c50-91fc-ed182d3112b1', expected)

    def test_data(self):
        obj = self.get_conferenceobj()
        expected = {'url': 'http://url.com', '_id': '759839e1-5d29-5c50-91fc-ed182d3112b1', 'deadline': 'deadline', 'metadata.worker': {'websiteUrl': 'website_url', 'dateExtracted': 'date_extracted', 'website': 'domain_url', 'domain': 'domain_name'}, 'title': 'title'}
        self.assertEqual(obj.data(), expected)

    def test_query_dict(self):
        obj = self.get_conferenceobj()
        expected = {'url': 'http://url.com', '_id': '759839e1-5d29-5c50-91fc-ed182d3112b1', 'deadline': 'deadline', 'metadata.worker': {'websiteUrl': 'website_url', 'dateExtracted': 'date_extracted', 'website': 'domain_url', 'domain': 'domain_name'}, 'title': 'title'}
        self.assertEqual(obj.query_dict(), expected)

    def test__str__(self):
        obj = self.get_conferenceobj()
        self.assertEqual(
            "{}".format(obj.querydata), obj.querydata.__str__()
        )

    def test_getitem(self):
        obj = self.get_conferenceobj()
        expected = "http://url.com"
        self.assertEqual(obj.__getitem__("url"), expected)

if __name__ == '__main__':
    unittest.main() 
