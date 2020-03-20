import requests
import math

class AdaptiveRequest:
    def __init__(self):
        self.max_wait_time = 1
        self.num_fail = 0
    def get(self , link ):
        try:
            res = requests.get(link , timeout = self.max_wait_time)
            return res
        except (requests.HTTPError , requests.ConnectionError) as err:
            self.num_fail= self.num_fail+1
            self.max_wait_time = 1+ math.exp(self.num_fail) 
            raise err