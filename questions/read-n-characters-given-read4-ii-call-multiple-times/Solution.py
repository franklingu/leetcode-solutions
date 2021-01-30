"""

None
"""


"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.end = False
        self.chars = []
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        if self.end and len(self.chars) == 0:
            return 0
        if len(self.chars) >= n or self.end:
            clen = min(len(self.chars), n)
            for i in range(clen):
                buf[i] = self.chars[i]
            self.chars = self.chars[clen:]
            return clen
        l = len(self.chars)
        for i in range(len(self.chars)):
            buf[i] = self.chars[i]
        self.chars = []
        curr = [''] * 4
        while n > l and not self.end:
            cnt = read4(curr)
            if cnt < 4:
                self.end = True
            clen = min(cnt, n - l)
            for i in range(clen):
                buf[l + i] = curr[i]
            l += clen
            for i in range(cnt - clen):
                self.chars.append(curr[i + clen])
        return l