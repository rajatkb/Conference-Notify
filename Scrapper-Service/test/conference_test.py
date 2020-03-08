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

    def test_getitem(self):
        obj = self.get_conferenceobj()
        expected = "http://url.com"
        self.assertEqual(obj.__getitem__("url"), expected)

    def test_title_type(self):
        obj = self.get_conferenceobj()
        res = type(obj.title).__name__
        expected = "str"
        self.assertEqual(res, expected)

    def test_url_type(self):
        obj = self.get_conferenceobj()
        res = type(obj.url).__name__
        expected = "str"
        self.assertEqual(res, expected)

    ## TO-DO  
    # Flaw in logic need to fix
    def test_deadline_type(self):
        obj = self.get_conferenceobj()
        res = type(obj.submission_deadline).__name__
        expected = "datetime"
        self.assertEqual(res, expected)

    def test_querydata_type(self):
        obj = self.get_conferenceobj()
        res = type(obj.querydata).__name__
        expected = "dict"
        self.assertEqual(res, expected)

    ## TO-DO 
    # flaw in logic need to fix
    def test_query_deadline_type(self):
        obj = self.get_conferenceobj()
        res = type(obj.querydata["deadline"]).__name__
        expected = "datetime"
        self.assertEqual(res, expected)
        
    def test_query_title_type(self):
        obj = self.get_conferenceobj()
        res = type(obj.querydata["title"]).__name__
        expected = "str"
        self.assertEqual(res, expected)


    def test_query_url_type(self):
        obj = self.get_conferenceobj()
        res = type(obj.querydata["url"]).__name__
        expected = "str"
        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main() 
