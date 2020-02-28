from .metadata import Metadata 
import base64

class Conference:

    @staticmethod
    def index():
        """Get fields for indexing
        
        Returns:
            List[(String , Boolean)] -- List of fields that should be indexed along with should it be unique or not. 
        """
        return [('url' , False) , ('deadline' , False) , ('title' , False)]

    def __init__(self, title , url , deadline , metadata, **kwargs):
        """[Conference class]
            Used for modeling the data of conferences
        
        Arguments:
            title {[string]} -- title of conference
            url {[string]} -- url of conference
            deadline {[datetime , string]} -- submission deadline
            metadata {Metadata} -- contains meta information
            **kwargs
            date_range : array[datetime , datetime] 
            location: string
            notificationdue: datetime 
            finaldue: datetime 
            categories: array[string]
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
        self.querydata.update(metadata.query_dict())
        ## Db compatibility 
        self._id = base64.b64encode(self.url) 
        ## A conference is bound to have unique link
        self.querydata['_id'] = self._id

    def data(self):
        return self.querydata
    
    def query_dict(self):
        return self.querydata

    def __str__(self):
        return str(self.querydata)
    
    def __getitem__(self , attr):
        return self.querydata[attr]

    