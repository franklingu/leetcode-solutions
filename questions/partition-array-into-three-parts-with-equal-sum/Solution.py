"""

Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.
Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])
 
Example 1:

Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:

Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false

Example 3:

Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

 
Constraints:

3 <= arr.length <= 5 * 104
-104 <= arr[i] <= 104


"""


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        if s % 3 != 0:
            return False
        s3 = s // 3
        ss = [0]
        tr = {}
        for i, a in enumerate(arr):
            ss.append(ss[-1] + a)
            tr[ss[-1]] = tr.get(ss[-1], []) + [i]
        if s3 not in tr or s3 + s3 not in tr:
            return False
        part1 = tr[s3]
        part2 = tr[s3 + s3]
        part3 = tr[s]
        for p in part2:
            if p > part1[0]:
                for j in part3:
                    if j > p:
                        return True
                else:
                    return False
        return False