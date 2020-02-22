import logging
import json
import argparse
import importlib

parser = argparse.ArgumentParser()
parser.add_argument("-c" , "--config" , default='config.json' , type=str , action='store' , dest="config")
parser.add_argument("-l" , "--log" , default="debug"  , action='store' , dest="log_level")
values = parser.parse_args()

level_defaults = {"debug":logging.DEBUG , "warn":logging.WARN , "info":logging.INFO , "error":logging.ERROR}

CONFIG = values.config
if values.log_level not in level_defaults:
    raise ValueError("Unsupported log level. Supported levels: DEBUG , WARN , INFO , ERROR")
log_level = level_defaults[values.log_level] 

if __name__ == '__main__':
    with open(CONFIG) as file:
        configuration = json.load(file)
    import_list = configuration["load"]
    for attr in import_list:
        path = attr["filename"]
        class_name = attr["class"]
        plugin_module = importlib.import_module(path , ".")
        scrapper = plugin_module.__getattribute__(class_name)
        scrapper(log_level , **configuration).run()