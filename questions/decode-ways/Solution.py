"""

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "111" can have each of its "1"s be mapped into 'A's to make "AAA", or it could be mapped to "11" and "1" ('K' and 'A' respectively) to make "KA". Note that "06" cannot be mapped into 'F' since "6" is different from "06".
Given a non-empty string num containing only digits, return the number of ways to decode it.
The answer is guaranteed to fit in a 32-bit integer.
 
Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0. The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20".
Since there is no character, there are no valid ways to decode this since all digits need to be mapped.

Example 4:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because the zero at the beginning of the string can't make a valid character. 

 
Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).


"""


class Solution:
    def numDecodings(self, s: str) -> int:
        def num_to_decode(s, index, track):
            if index > len(s):
                return 0
            elif index == len(s):
                return 1
            if index in track:
                return track[index]
            if s[index] == '0':
                return 0
            v1 = num_to_decode(s, index + 1, track)
            if 1 <= int(s[index:index + 2]) <= 26:
                v2 = num_to_decode(s, index + 2, track)
            else:
                v2 = 0
            ret = v1 + v2
            track[index] = ret
            return ret
        
        track = {}
        return num_to_decode(s, 0, track)