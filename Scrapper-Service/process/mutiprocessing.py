## TO_DO
## 1. Add multiprocessing from the reference implementation
## 2. Use Logging at properplaces for generating logs from the context manager
## 3. folow the main class to know where to grab the log level and how to get a logger
class MultiProcessingContext:
    def __init__(self , log_level , log_stream):
        """[Multi Processing class]
            Responsible for running the lambda functions passed in
            inside threads
        """
        pass
    def __execute__(self , runnable):
        runnable()
        pass
    def __enter__(self):
        return self.__execute__ 

    def __exit__(self , exception_type, exception_value, traceback):
        pass

## A HELPER IMPLEMENTATION
# class MultiPoc:
#     def __init__(self):
#         self.process_list = []
#         pass
#     def __execute__(self , runnable ):
#         p = Process(target= runnable)
#         self.process_list.append(p)
#         p.start()
#     def __enter__(self):
#         return self.__execute__
    
#     def __exit__(self , exception_type, exception_value, traceback):
#         for process in self.process_list:
#             process.join()