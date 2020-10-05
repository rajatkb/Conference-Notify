import requests
import math
import backoff

class AdaptiveRequest:
    def __init__(self):
        self.max_wait_time = 10

    @backoff.on_exception(
        backoff.expo, #exponential backoff
        (requests.HTTPError , requests.ConnectionError), #retry if errors encountered
        max_time=300 #give up after 300 seconds time
    )
    def get(self , link , **kwargs):
        return requests.get(link , timeout = self.max_wait_time , **kwargs)
