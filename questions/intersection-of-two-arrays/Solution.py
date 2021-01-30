"""

Given two arrays, write a function to compute their intersection.
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]


Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:

Each element in the result must be unique.
The result can be in any order.

 

"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ### method1: using set
        # return list(set(nums1).intersection(set(nums2)))
        ### method2: using sort + linear merge
        # nums1.sort()
        # nums2.sort()
        # idx1, idx2 = 0, 0
        # ret = []
        # while idx1 < len(nums1) and idx2 < len(nums2):
        #     n1, n2 = nums1[idx1], nums2[idx2]
        #     if n1 == n2:
        #         if not ret or ret[-1] != n1:
        #             ret.append(n1)
        #         idx1 += 1
        #         idx2 += 1
        #     elif n1 < n2:
        #         idx1 += 1
        #     else:
        #         idx2 += 1
        # return ret
        ### method3: using sort + binary search
        def binary_search_match(nums, start, target):
            clen = 2
            while start + clen < len(nums) and nums[start + clen] < target:
                clen <<= 1
            end = min(start + clen, len(nums) - 1)
            if nums[end] < target:
                return True, None, start
            while start < end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    start = mid
                    break
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            match = None
            if start < len(nums) and nums[start] == target:
                match = target
                start += 1
            return False, match, start
        
        nums1.sort()
        nums2.sort()
        ret = []
        start1, start2 = 0, 0
        while start1 < len(nums1) and start2 < len(nums2):
            n1, n2 = nums1[start1], nums2[start2]
            if n1 == n2:
                if not ret or ret[-1] != n1:
                    ret.append(n1)
                start1 += 1
                start2 += 1
            elif n1 < n2:
                done_search, match, start1 = binary_search_match(nums1, start1, n2)
                if done_search:
                    break
                if match is not None:
                    if not ret or ret[-1] != match:
                        ret.append(match)
                start2 += 1
            else:
                done_search, match, start2 = binary_search_match(nums2, start2, n1)
                if done_search:
                    break
                if match is not None:
                    if not ret or ret[-1] != match:
                        ret.append(match)
                start1 += 1
        return ret