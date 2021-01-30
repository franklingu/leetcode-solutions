"""

Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.
A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 
 
Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:
Input: s = "1111"
Output: ["1.1.1.1"]
Example 4:
Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
Example 5:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

 
Constraints:

0 <= s.length <= 3000
s consists of digits only.


"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def generateInterpretations(s, index, positions, ret):
            if index > len(s) or (index == len(s) and len(positions) < 3):
                return
            if index == len(s) or len(positions) == 3:
                runner = 0
                tmp = []
                for i, ch in enumerate(s):
                    if runner == 3:
                        tmp.append(ch)
                        continue
                    if i == positions[runner]:
                        runner += 1
                        tmp.append('.')
                        tmp.append(ch)
                    else:
                        tmp.append(ch)
                ret.append(''.join(tmp))
                return
            generateInterpretations(s, index + 1, positions, ret)
            start = 0 if not positions else positions[-1]
            if index > start + 1 and s[start] == '0':
                return
            elif int(s[start:index]) > 255:
                return
            elif len(positions) == 2:
                if s[index] == '0' and index < len(s) - 1:
                    return
                elif int(s[index:]) > 255:
                    return
            positions.append(index)
            generateInterpretations(s, index + 1, positions, ret)
            positions.pop() 
        
        ret = []
        generateInterpretations(s, 1, [], ret)
        return ret