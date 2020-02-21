import requests
import logging
from bs4 import BeautifulSoup

from Scrappers import WikiCfpScrapper

WikiCfpScrapper(logging.INFO).run()