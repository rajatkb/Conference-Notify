class Conference:

    @staticmethod
    def index():
        """Get fields for indexing
        
        Returns:
            List[String] -- List of fields that should be indexed. 
        """
        return ['deadline']

    def __init__(self, title , url , deadline ,  **kwargs):
        """[Conference class]
            Used for modeling the data of conferences
        
        Arguments:
            title {[string]} -- title of conference
            url {[string]} -- url of conference
            deadline {[datetime , string]} -- submission deadline

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
        self.dict_data = kwargs
        self.dict_data["title"] = title
        self.dict_data["url"] = url
        self.dict_data["deadline"] = deadline
        ## Db compatibility 
        self._id = hash(self.url) ## A conference is bound to have unique link
        self.dict_data['_id'] = self._id

    def data(self):
        return self.dict_data

    def __str__(self):
        return str(self.dict_data)
    
    def __getitem__(self , attr):
        return self.dict_data[attr]

    