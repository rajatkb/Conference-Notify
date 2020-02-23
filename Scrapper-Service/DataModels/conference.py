from .metadata import Metadata 

class Conference:

    @staticmethod
    def index():
        """Get fields for indexing
        
        Returns:
            List[(String , Boolean)] -- List of fields that should be indexed along with should it be unique or not. 
        """
        return [('url' , True) , ('deadline' , False)]

    def __init__(self, title , url , deadline , metadata, **kwargs):
        """[Conference class]
            Used for modeling the data of conferences
        
        Arguments:
            title {[string]} -- title of conference
            url {[string]} -- url of conference
            deadline {[datetime , string]} -- submission deadline
            metadata {Metadata} -- contains meta information
            **kwargs
            date_range : array of two dates 
            location: string
            notificationdue: datetime object
            finaldue: datetime object
            categories: array of string
            bulk_text: string 
        """
        ## Cleaning title text
        title = title.split(" ")
        title = list(map(lambda x: x.strip() , title))
        title = " ".join(title)
        self.title = title
        self.url = url.strip()
        self.submission_deadline = deadline
        self.querydata = kwargs
        self.querydata["title"] = title
        self.querydata["url"] = url
        self.querydata["deadline"] = deadline
        self.querydata.update(metadata.data())
        ## Db compatibility 
        self._id = hash(self.url) ## A conference is bound to have unique link
        self.querydata['_id'] = self._id

    def data(self):
        return self.querydata

    def __str__(self):
        return str(self.querydata)
    
    def __getitem__(self , attr):
        return self.querydata[attr]

    