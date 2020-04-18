import logging

LOG_STREAM_OPTIONS = ["console" , "file"]

LOG_LEVEL_DEFAULTS = {
    "debug": logging.DEBUG,
    "warn": logging.WARN,
    "info": logging.INFO,
    "error": logging.ERROR,
}

LOG_LEVEL_OPTIONS = LOG_LEVEL_DEFAULTS.keys()

def get_logger(context_name , log_level , log_stream_option , log_folder="logs"):
    
    if log_stream_option == "file":
        log_stream = logging.FileHandler( "{}/{}.log".format(log_folder , context_name) )
    elif log_stream_option == "console":
        log_stream = logging.StreamHandler()
    else:
        raise ValueError("Bad log stream option given , legal values : {}".format(LOG_STREAM_OPTIONS))

    if not log_level in LOG_LEVEL_OPTIONS:
        raise ValueError("Bad log level value given , legal values :{}".format(LOG_STREAM_OPTIONS)) 
    log_level = LOG_LEVEL_DEFAULTS[log_level]

    logger = logging.getLogger(context_name)
    logger.setLevel(log_level)
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_stream.setFormatter(log_format)
    logger.addHandler(log_stream)
    # Works as a separator , more readable logs
    return logger

def print_start(logger):
    logger.info('''
    
  _________                  .__                         __                  __   
 /   _____/ ______________  _|__| ____  ____     _______/  |______  ________/  |_ 
 \_____  \_/ __ \_  __ \  \/ /  |/ ___\/ __ \   /  ___/\   __\__  \ \_  __ \   __|
 /        \  ___/|  | \/\   /|  \  \__\  ___/   \___ \  |  |  / __ \|  | \/|  |  
/_______  /\___  >__|    \_/ |__|\___  >___  > /____  > |__| (____  /__|   |__|  
        \/     \/                    \/    \/       \/            \/             
    
    ''')