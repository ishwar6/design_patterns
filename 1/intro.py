## Without Pattern

# Example 1: Logging System in a High-Performance Application
class Logger:
  def __init__(self, file):
    self.file = open("file", "a")

  def write_log(self, message):
    self.file.write(message + "\a")
    self.file.flush()

  def close(self):
    self.file.close()


# Every time the application needs to log, a new logger instance is created, leading to inconsistencies and performance issues.
# Problem: Multiple logger instances
logger1 = Logger()
logger1.write_log("Transaction started.")
logger1.close()

logger2 = Logger()
logger2.write_log("Transaction completed.")
logger2.close()


# Issues:
# Multiple instances lead to scattered log handling.
# If switching to a cloud-based logger, changes are required in multiple places.

##############################################################################################################################################################################
#################################################################### Logger with Singleton Pattern ##########################################################################
# With Singleton:
# A single logger instance ensures centralized log management.

class SingletonLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonLogger, cls).__new__(cls, *args, **kwargs)
            cls._instance.file = open("logfile.txt", "a")
        return cls._instance

    def write_log(self, message):
        self.file.write(message + "\n")
        self.file.flush()

    def close(self):
        self.file.close()

# Single logger instance
logger1 = SingletonLogger()
logger1.write_log("Transaction started.")

logger2 = SingletonLogger()
logger2.write_log("Transaction completed.")

# if we have to use logger across multiple files
# Both loggers are the same instance
logger1.close()


##############################################################################################################################################################################
#################################################################### Logger with Singleton Pattern ##########################################################################

# Benefits:
# Centralized logging ensures consistency.
# Changing the logging backend (e.g., file to cloud) requires minimal code modification.





