import logging
import json
import argparse
import importlib
import traceback
import os
from utility import str2bool , getLogger , printStart




##
#
# Test whether the initialization is working or not
# >> python app.py -l debug -ls console  --test True
# 
# Test whether the run is working or not
# >> python app.py -l debug -ls file --test False
#  
# 

parser = argparse.ArgumentParser()
parser.add_argument("-c" , "--config",  default='config.json' , type=str , action='store'
                                     ,  dest="config" , help="Specify config.json file")
parser.add_argument("-l" , "--log" ,    default="debug"  , action='store', dest="log_level" ,
                                        choices=["debug" , "warn" , "error" , "info"]  , help="Specify the debug level ,default: %(default)s")
parser.add_argument("-t" , "--test" ,   default=True , type=str2bool , action="store" , dest="test" , 
                                        help="Specify whether to test app initialization or run the scrappers ,default: %(default)s")
parser.add_argument("-ls", "--logStream", default="console", type=str , action="store" , dest="log_stream" , 
                                          choices=["console" , "file"],
                                          help="Specify whether to print logs on terminal or to file ,default: %(default)s"  )
values = parser.parse_args()

LOG_LEVEL_DEFAULTS = {"debug":logging.DEBUG , "warn":logging.WARN , "info":logging.INFO , "error":logging.ERROR}
LOG_STREAM_DEFAULTS = { "file":lambda filename:logging.FileHandler(filename),
                        "console":lambda filname: logging.StreamHandler()
                        }

if values.log_level.lower() not in LOG_LEVEL_DEFAULTS:
    raise ValueError("Unsupported log level. Supported levels: debug , warn , info , error")
if values.log_stream.lower() not in LOG_STREAM_DEFAULTS:
    raise ValueError("Unsupported log stream. Supported levels: file , console")

log_level = LOG_LEVEL_DEFAULTS[values.log_level.lower()]

istest = values.test

CONFIG = values.config

log_streamOption = LOG_STREAM_DEFAULTS[values.log_stream.lower()]
 

def createDatabase(configuration):
    db_configuration = configuration["database"]
    path = db_configuration["plugin"]["filename"]
    classname = db_configuration["plugin"]["class"]
    module = importlib.import_module(path , ".")
    Database = module.__getattribute__(classname)
    return lambda logger: Database(logger , **db_configuration) 

if __name__ == '__main__':

    with open(CONFIG) as file:
        configuration = json.load(file)
    
    logging_configuration = configuration["logging"]
    log_folder = logging_configuration["output"]
    if not log_folder in os.listdir('.'):
        os.mkdir(log_folder)
    
    logger = getLogger(__name__ , log_level ,  log_streamOption("{}/{}.log".format(log_folder , "main")) )

    printStart(logger)
    logger.info("Application started , Extracting all the plugins")

    import_list = configuration["plugins"]
    for attr in import_list:

        path = attr["filename"]
        class_name = attr["class"]
        plugin_module = importlib.import_module(path , ".")
        scrapper = plugin_module.__getattribute__(class_name)
        try:
            log_stream = log_streamOption("{}/{}.log".format(log_folder , class_name))
            if istest:
                scrapper( log_level = log_level, log_stream = log_stream , getDatabaseObject = createDatabase(configuration) )
            else:
                scrapper( log_level = log_level, log_stream = log_stream , getDatabaseObject = createDatabase(configuration) ).run()
        except Exception as e:
            logger.error("{} scrapper failed".format(class_name))
            traceback.print_exception(type(e), e, e.__traceback__)
    logger.info("Scrapping done from all Scrapper plugins")