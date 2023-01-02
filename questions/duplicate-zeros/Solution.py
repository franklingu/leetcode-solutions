"""

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
 
Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

 
Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9


"""


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx, cnt = 0, 0
        while cnt < len(arr):
            elem = arr[idx]
            if elem == 0:
                cnt += 2
            else:
                cnt += 1
            idx += 1
        cnt -= 1
        idx -= 1
        if cnt == len(arr):
            cnt -= 1
            arr[cnt] = arr[idx]
            idx -= 1
            cnt -= 1
        while idx >= 0:
            if idx == cnt:
                break
            elem = arr[idx]
            idx -= 1
            arr[cnt] = elem
            cnt -= 1
            if elem == 0:
                arr[cnt] = elem
                cnt -= 1