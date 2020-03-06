class Metadata:
    def __init__(self , worker , date_extracted , website_url , domain_url , domain_name  , **kwargs):
        """Container for meta information inserted by the parser
        
        Arguments:
            worker {[string]} -- current worker thread 
            date_extracted {[type]} -- which date information was extracted
            website_url {[type]} -- the url of the page 
            domain {[type]} -- domain address
        """
        self.worker = worker
        self.key = "metadata."+worker
        self.querydata = {
            self.key: {
                "dateExtracted":date_extracted,
                "websiteUrl":website_url,
                "website":domain_url,
                "domain":domain_name
            }
        }
        self.querydata[self.key].update(kwargs)


    def data(self):
        return self.querydata[self.key]
    
    def query_dict(self):
        return self.querydata

    def __str__(self):
        return str(self.querydata)
    
    def __getitem__(self , attr):
        return self.querydata[self.key][attr]