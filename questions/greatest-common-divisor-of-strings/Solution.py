"""
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        def made_of(s, part, c):
            for i in range(0, len(s), c):
                p = s[i:i + c]
                if p != part:
                    return False
            return True
        
        if not str1 or not str2:
            return ''
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        c = gcd(len(str1), len(str2))
        if made_of(str1, str2[:c], c) and made_of(str2, str1[:c], c):
            return str1[:c]
        return ''


class Solution2:
    def gcdOfStrings(self, str1, str2):
        # Euclidean Algorithm
        if len(str1) < len(str2): 
                str1, str2 = str2, str1
		# now can assume len(str1) >= len(str2)
		
        DIV = True
        while DIV:
            DIV = False
            n, m = len(str1), len(str2)                
            
            while(str1[:m] == str2):
                DIV = True
                str1 = str1[m:]
            if not str1: # divisible
                return str2 
            else:
                str1, str2 = str2, str1
                
        return ""