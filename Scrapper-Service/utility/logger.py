import logging

def getLogger(context_name , log_level , log_stream):
    logger = logging.getLogger(context_name)
    logger.setLevel(log_level)
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_stream.setFormatter(log_format)
    logger.addHandler(log_stream)
    # Works as a separator , more readable logs
    return logger

def printStart(logger):
    logger.info('''
    
  _________                  .__                         __                  __   
 /   _____/ ______________  _|__| ____  ____     _______/  |______  ________/  |_ 
 \_____  \_/ __ \_  __ \  \/ /  |/ ___\/ __ \   /  ___/\   __\__  \ \_  __ \   __|
 /        \  ___/|  | \/\   /|  \  \__\  ___/   \___ \  |  |  / __ \|  | \/|  |  
/_______  /\___  >__|    \_/ |__|\___  >___  > /____  > |__| (____  /__|   |__|  
        \/     \/                    \/    \/       \/            \/             
    
    ''')