'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

'''
Maximum window technique
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mm = 0
        start = 0
        track = {}
        for i, c in enumerate(s):
            if c not in track:
                track[c] = i
                mm = max(mm, i - start + 1)
            else:
                prev = max(track[c], start - 1)
                curr_len = i - prev
                mm = max(mm, curr_len)
                start = prev + 1
                track[c] = i
        return mm
