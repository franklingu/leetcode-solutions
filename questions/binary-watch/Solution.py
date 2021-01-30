"""

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
Each LED represents a zero or one, with the least significant bit on the right.

For example, the above binary watch reads "3:25".
Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
Example:
Input: n = 1Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:

The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".


"""


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def transfer_reading(clock):
            hour = int(''.join(clock[:4]), 2)
            minute = int(''.join(clock[4:]), 2)
            if hour > 11:
                return None
            if minute > 59:
                return None
            return '{}:{:02d}'.format(hour, minute)
        
        def gen_cases(num, start=0, clock=None):
            if num < 0:
                return
            if start >= 10 and num > 0:
                return
            elif start >= 10 and num == 0:
                yield clock
                return
            if clock is None:
                clock = ['0'] * 10
            clock = list(clock)
            for gc in gen_cases(num, start + 1, clock):
                yield gc
            if start < 10:
                clock[start] = '1'
                for gc in gen_cases(num - 1, start + 1, clock):
                    yield gc
        
        ret = []
        for clock in gen_cases(num):
            reading = transfer_reading(clock)
            if reading is None:
                continue
            ret.append(reading)
        return ret
        