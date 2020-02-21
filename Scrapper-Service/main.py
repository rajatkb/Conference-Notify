import requests
import logging
from bs4 import BeautifulSoup

from Scrappers import WikiCfpScrapper

WikiCfpScrapper(logging.DEBUG ,database_name='Conference_Notify', collection_name='confernce', host = 'localhost' , port = 27017).run()