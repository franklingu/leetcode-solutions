"""

Given two arrays, write a function to compute their intersection.
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]


Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ### method 1
        # nums1.sort()
        # nums2.sort()
        # ret = []
        # runner1, runner2 = 0, 0
        # while runner1 < len(nums1) and runner2 < len(nums2):
        #     if nums1[runner1] == nums2[runner2]:
        #         ret.append(nums1[runner1])
        #         runner1 += 1
        #         runner2 += 1
        #     elif nums1[runner1] > nums2[runner2]:
        #         runner2 += 1
        #     else:
        #         runner1 += 1
        # return ret
        ### method 2
        # import collections
        # ns1 = collections.Counter(nums1)
        # ns2 = collections.Counter(nums2)
        # ret = []
        # for k, v in ns1.iteritems():
        #     if k not in ns2:
        #         continue
        #     v = min(v, ns2[k])
        #     ret.extend([k] * v)
        # return ret
        ### method 3
        def binary_search_match(nums, start, target):
            clen = 2
            while start + clen < len(nums) and nums[start + clen] < target:
                clen <<= 1
            end = min(start + clen, len(nums) - 1)
            if nums[end] < target:
                return True, None, start
            while start < end:
                mid = (start + end) // 2
                if nums[mid] >= target:
                    end = mid
                else:
                    start = mid + 1
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
                ret.append(n1)
                start1 += 1
                start2 += 1
            elif n1 < n2:
                done_search, match, start1 = binary_search_match(nums1, start1, n2)
                if done_search:
                    break
                if match is not None:
                    ret.append(match)
                start2 += 1
            else:
                done_search, match, start2 = binary_search_match(nums2, start2, n1)
                if done_search:
                    break
                if match is not None:
                    ret.append(match)
                start1 += 1
        return ret