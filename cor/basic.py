#chain of responsibility is like customer care service: first call goes to junior executive -> he/she than send it to senior -> and so on. 
#So this makes a way to ensure that customer queries are handled efficiently, with each query being addressed by the most appropriate team member based on its complexity.




from abc import ABC, abstractmethod

class Logger:
    DEBUG, INFO, WARNING, ERROR, CRITICAL = range(5)
    
    def __init__(self, level):
        self.level = level
        self.next = None
        
    def set_next(self, next):
        self.next = next

    #here log method will call the next if in each case till current level is smaller than log level. 
    def log(self, level, message):
        if level >= self.level:
            self.write_message(message)
        if self.next is not None:
            self.next.log(level, message)

    @abstractmethod
    def write_message(self, message):
        pass
    

class DebugLogger(Logger):
    def write_message(self, message):
        print(f"DEBUG: {message}")
        

class InfoLogger(Logger):
    def write_message(self, message):
        print(f"INFO: {message} added to file")
        

class WarningLogger(Logger):
    def write_message(self, message):
        print(f"Warning: {message} sent on just dev on mail")

class ErrorLogger(Logger):
    def write_message(self, message):
        print(f"ERROR: {message} sent on mail to all dev")
        
        
        
#client code

debug_logger = DebugLogger(Logger.DEBUG)
info_logger = InfoLogger(Logger.INFO)
warning_logger = WarningLogger(Logger.WARNING)
error_logger = ErrorLogger(Logger.ERROR)

#lets meke the chain. 
debug_logger.set_next(info_logger)
info_logger.set_next(warning_logger)
warning_logger.set_next(error_logger)


#use it from first in the chain
debug_logger.log(Logger.INFO, "this is info log")

debug_logger.log(Logger.ERROR, "this is error log")


#output: 
# DEBUG: this is info log
# INFO: this is info log added to file

#output of 2nd case: 
# DEBUG: this is error log
# INFO: this is error log added to file
# Warning: this is error log sent on just dev on mail
# ERROR: this is error log sent on mail to all dev


            
