"""

The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].

Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
 
Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

 
Constraints:

1 <= num.length <= 104
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 104


"""


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        def int_to_arr(val):
            ret = []
            while val > 0:
                val, c = divmod(val, 10)
                ret.append(c)
            return ret[::-1]
            
        def add_arrs(arr1, arr2):
            ret = []
            carry = 0
            for a, b in itertools.zip_longest(reversed(arr1), reversed(arr2), fillvalue=0):
                carry, c = divmod(a + b + carry, 10)
                ret.append(c)
            if carry != 0:
                ret.append(carry)
            return ret[::-1]
        
        return add_arrs(num, int_to_arr(k))