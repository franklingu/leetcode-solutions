/**
 * There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median
 * of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
 */

public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1 == null || nums2 == null) {
            return 0.0;  // should throw exception
        }
        if (nums1.length == 0 && nums2.length == 0) {
            return 0.0;
        } else if (nums1.length == 0) {
            return (nums2.length % 2 == 0) ? (nums2[nums2.length / 2] + nums2[nums2.length / 2 - 1]) / 2.0 : nums2[nums2.length / 2];
        } else if (nums2.length == 0) {
            return (nums1.length % 2 == 0) ? (nums1[nums1.length / 2] + nums1[nums1.length / 2 - 1]) / 2.0 : nums1[nums1.length / 2];
        }
        boolean isMSmaller = nums1.length < nums2.length;
        int[] temp;
        int tempInt;
        if (!isMSmaller) {
            temp = nums2;
            nums2 = nums1;
            nums1 = temp;
        }
        int M = nums1.length, N = nums2.length;
        if (M < N && nums1[M - 1] <= nums2[0]) {
            return ((M + N) % 2 == 0) ? (nums2[(M + N) / 2 - M] + nums2[(M + N) / 2 - M - 1]) / 2.0 : nums2[(M + N) / 2 - M];
        }
        int start1 = 0, end1 = M, start2 = 0, end2 = N, mid1 = 0, mid2 = 0;
        while (start1 < end1 && start2 < end2) {
            // System.out.format("%d %d  %d %d\n", start1, end1, start2, end2);
            mid1 = (start1 + end1) / 2;
            mid2 = (start2 + end2) / 2;
            if (nums1[mid1] > nums2[mid2]) {
                start2 = mid2;
                end2 = start2 + (end1 - mid1);
                end1 = mid1;
            } else if (nums1[mid1] < nums2[mid2]) {
                end2 = mid2;
                start2 = end2 + (start1 - mid1);
                start1 = mid1;
            } else {
                break;
            }
        }
        // System.out.format("%d %d  %d %d\n", start1, end1, start2, end2);
        if ((M + N) % 2 == 0) {
            mid1 = (start1 + end1) / 2;
            mid2 = (start2 + end2) / 2;
            if (mid1 + mid2 == (M + N) / 2 - 1) {
                
            } else if (mid1 + mid2 > (M + N) / 2 - 1) {
                
            } else {
                
            }
        } else {
            if (start1 == end1) {
                return (double)nums1[(start1 + end1) / 2];
            } else {
                return (double)nums2[(start2 + end2) / 2];
            }
        }
    }
}
