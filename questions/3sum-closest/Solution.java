/**
 * Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
 * Return the sum of the three integers. You may assume that each input would have exactly one solution.
 *
 *   For example, given array S = {-1 2 1 -4}, and target = 1.
 *   The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 */

public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        if (nums == null || nums.length <= 2) {
            return -1;  // should throw exception probably
        }
        Arrays.sort(nums);
        int closest = nums[0] + nums[2] + nums[1];
        for (int i = 0; i < nums.length - 2; i++) {
            int start = i + 1;
            int end = nums.length - 1;
            int temp;
            while (start < end) {
                temp = nums[start] + nums[end] + nums[i];
                if (temp - target == 0) {
                    return target;
                } else if (temp - target < 0) {
                    start++;
                } else {
                    end--;
                }
                if (Math.abs(temp - target) < Math.abs(closest - target)) {
                    closest = temp;
                }
            }
        }
        
        return closest;
    }
}
