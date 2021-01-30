/**
 * Given an integer array, you need to find one continuous subarray that
 * if you only sort this subarray in ascending order, then the whole array
 * will be sorted in ascending order, too.
 *
 * You need to find the shortest such subarray and output its length.
 *
 * Example 1:
 *
 * Input: [2, 6, 4, 8, 10, 9, 15]
 * Output: 5
 * Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order
 * to make the whole array sorted in ascending order.
 *
 */
class Solution {
    public int findUnsortedSubarray(int[] nums) {
        if (nums.length < 1) {
            return 0;
        }
        int[] mins = new int[nums.length];
        int[] maxes = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                maxes[i] = nums[i];
            } else {
                if (maxes[i - 1] > nums[i]) {
                    maxes[i] = maxes[i - 1];
                } else {
                    maxes[i] = nums[i];
                }
            }
        }
        for (int i = nums.length - 1; i >= 0; i--) {
            if (i == nums.length - 1) {
                mins[i] = nums[i];
            } else {
                if (mins[i + 1] < nums[i]) {
                    mins[i] = mins[i + 1];
                } else {
                    mins[i] = nums[i];
                }
            }
        }
        int start = 0, end = nums.length - 1;
        while (start < end) {
            if (nums[start] >= maxes[start] && nums[start] <= mins[start]) {
                start++;
            } else {
                break;
            }
        }
        while (start < end) {
            if (nums[end] >= maxes[end] && nums[end] <= mins[end]) {
                end--;
            } else {
                break;
            }
        }
        if (start >= end) {
            return 0;
        } else {
            return end - start + 1;
        }
    }
}
