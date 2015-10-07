/**
 * Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
 * 
 * Note:
 * You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional
 * elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
 */

public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int runner = m + n - 1, runner1 = m - 1, runner2 = n - 1;
        
        while (runner >= 0) {
            if (runner1 < 0) {
                nums1[runner] = nums2[runner2];
                runner--;
                runner2--;
                continue;
            } else if (runner2 < 0) {
                nums1[runner] = nums1[runner1];
                runner--;
                runner1--;
                continue;
            }
            
            if (nums1[runner1] > nums2[runner2]) {
                nums1[runner] = nums1[runner1];
                runner1--;
            } else {
                nums1[runner] = nums2[runner2];
                runner2--;
            }
            runner--;
        }
    }
}
