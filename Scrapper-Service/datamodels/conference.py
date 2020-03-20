from .metadata import Metadata 
import datetime
import uuid

class Conference:

    @staticmethod
    def index():
        """Get fields for indexing
        Returns:
            List[(String , Boolean)] -- List of fields that should be indexed along with should it be unique or not. 
        """
        return [('url' , False) , ('deadline' , False) , ('title' , False) , ('categories' , False)]

    def __init__(self, title , url , deadline , metadata, **kwargs):
        """[Conference class]
            Used for modeling the data of conferences
        
        Arguments:
            title {[string]} -- title of conference
            url {[string]} -- url of conference
            deadline {[datetime , string]} -- submission deadline
            metadata {Metadata} -- contains meta information
            
            **kwargs
            dateRange : array[datetime , datetime] 
            location: string
            notificationDue: datetime 
            finalDue: datetime 
            categories: array[string]
            bulkText: string 
        """
        ## Cleaning title text
        title = title.split(" ")
        title = list(map(lambda x: x.strip() , title))
        title = " ".join(title)
        self.title = title
        self.url = url.strip()
        
        if not isinstance(deadline  , datetime.datetime):
            raise ValueError("deadline is not datetime") 
        
        if not isinstance(metadata , Metadata):
            raise ValueError("metadata passed is not instance of the Metadata data model")

        self.deadline = deadline
        
        self.querydata = kwargs
        self.querydata["title"] = title
        self.querydata["url"] = url
        self.querydata["deadline"] = deadline
        self.querydata.update(metadata.query_dict())
        ## Db compatibility 
        self._id = self.__generate_uuid()
        ## A conference is bound to have unique link
        self.querydata['_id'] = self._id

        categories = self.querydata.pop("categories",None)
        
        self.query = {"$set": self.querydata}
        
        if categories is not None:
            category_query = {"categories":{"$each":categories}}
            self.query["$push"]=category_query
        
        
    def __generate_uuid(self):
        return str(uuid.uuid5(uuid.NAMESPACE_URL,self.url))
        
    def get_query(self):
        """Returns the query dictionary usable for update and upsert
        Returns:
            [dictionary] -- [dictionary appropriate for using in update statement for inserting data in mongo]
        """
        return self.query

    def __str__(self):
        return str(self.querydata)
    
    def __getitem__(self , attr):
        return self.querydata[attr]

    