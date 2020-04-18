from utility import get_logger , print_start
from multiprocessing import Process
import dill

def dill_encode(runnable):
    runnable_serialized = dill.dumps(runnable)
    return runnable_serialized

def dill_decode_run(runnable_serialized):
    runnable_class , args = dill.loads(runnable_serialized)
    try:
        runnable_obj = runnable_class(**args)
        runnable_obj.run()
    except Exception as e:
        print("[dill routine]:  Runnable failed in runtime due to error raised {}".format(e))



class MultiProcessingContext:
    
    def __init__(self , log_level , log_stream , log_folder="logs"):
        """[Multi Processing class]
            Responsible for running the lambda functions passed in
            inside threads
            Arguments:
                log_level {[string]} -- Levels of log for each process
                log_stream {[string]} -- Stream of log for each process
                
        """
        self.logger = get_logger(__name__, log_level, log_stream , log_folder)
        self.process_list=[]
    
    def __execute__(self , runnable , **kwargs):
        """Start execution of MultiProcessingContext 
            Returns:
                None
        """
        self.logger.info(''' 
                          Thread Process initiated
                         ''')
        ## start process for each call

        serialized = dill_encode((runnable , kwargs))
        p= Process(target= dill_decode_run , args=(serialized,))
        ## append the each process in list
        self.process_list.append(p)
        ## start calling process
        p.start()

    def __enter__(self):
        return self.__execute__ 

    def __exit__(self , exception_type, exception_value, traceback):
        ## job of each process is completed
        for process in self.process_list:
            process.join()

