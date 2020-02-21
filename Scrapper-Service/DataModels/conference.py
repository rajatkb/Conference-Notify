class Conference:
    def __init__(self, title , url , deadline ,  **kwargs):
        """ [Conference class]
            Used for modeling the data of conferences
        """
        self.title = title
        self.url = url
        self.date_range = kwargs['date_range']
        self.location = kwargs['location']
        self.submission_deadline = deadline
        self.notification_due = kwargs['notificationdue']
        self.final_version_due = kwargs['finaldue']
        self.categories = kwargs['categories']
        self.bulk_text = kwargs['bulk_text']
        self.dict_data = kwargs
        self.dict_data["title"] = title
        self.dict_data["url"] = url
        self.dict_data["deadline"] = deadline

    def __str__(self):
        return str(self.dict_data)
    
    def __getitem__(self , attr):
        return self.dict_data[attr]