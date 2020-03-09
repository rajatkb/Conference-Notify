from utility import get_logger , print_start

## TO_DO
## 1. Add multiprocessing from the reference implementation
## 2. Use Logging at properplaces for generating logs from the context manager
class MultiProcessingContext:
    def __init__(self , log_level , log_stream):
        """[Multi Processing class]
            Responsible for running the lambda functions passed in
            inside threads
        """
        self.logger = get_logger(__name__ , log_level , log_stream)

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