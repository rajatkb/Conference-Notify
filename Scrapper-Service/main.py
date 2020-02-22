import logging
import json
import argparse
from Scrappers import WikiCfpScrapper


WikiCfpScrapper(logging.DEBUG ,database_name='Conference_Notify', collection_name='conference', host = 'localhost' , port = 27017)