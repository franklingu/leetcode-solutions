"""

None
"""


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.track = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.track:
            ret = True
        else:
            ret = timestamp - self.track[message] >= 10
        if ret:
            self.track[message] = timestamp
        return ret


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)