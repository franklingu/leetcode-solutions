/**
 * Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
 * 
 * For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
 * the contiguous subarray [4,−1,2,1] has the largest sum = 6.
 */

public class Solution {
    public int maxSubArray(int[] nums) {
        if (nums == null || nums.length <= 0) {
            return 0;
        }
        int sum = 0, maxSofar = nums[0];
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            maxSofar = Math.max(maxSofar, sum);
            if (sum < 0) {
                sum = 0;
            }
        }
        
        return maxSofar;
    }
}
