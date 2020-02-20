from collections import deque



class Scrapper:
    def __init__(self ,  start_link:str = "", wait_between_request:int = 0):
        self.start_link = start_link
        self.wait_between_request = wait_between_request

    def __walk__(self):
        pass