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

