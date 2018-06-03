/**
 * Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
 *
 * Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
 *
 * Note: You are not suppose to use the library's sort function for this problem.
 *
 * Example:
 *
 * Input: [2,0,2,1,1,0]
 * Output: [0,0,1,1,2,2]
 *
 * Follow up:
 *
 *   A rather straight forward solution is a two-pass algorithm using counting sort.
 *   First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
 *   Could you come up with a one-pass algorithm using only constant space?
 *
 */

import java.util.*;

class Solution {
    public void sortColors(int[] nums) {
        int start = 0;
        int end = nums.length;
        int id0 = 0, id1 = 0, num = 0;
        while (start < end) {
            num = nums[start];
            nums[start] = 2;
            if (num == 0) {
                nums[id0] = 0;
                if (id1 != id0) {
                    nums[id1] = 1;
                }
                id1++;
                id0++;
            } else if (num == 1) {
                nums[id1] = 1;
                id1++;
            }
            start++;
            // System.out.println(Arrays.toString(nums));
        }
    }
}

