class Multiprocessing:
    def __init__(self):
        """[Multi Processing class]
            Responsible for running the lambda functions passed in
            inside threads
        """
        pass
    def execute_process(self ,  runnable = lambda : None ):
        runnable()