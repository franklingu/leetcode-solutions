/**
 * Given an array of non-negative integers, you are initially positioned at the
 * first index of the array.
 *
 * Each element in the array represents your maximum jump length at that position.
 *
 * Determine if you are able to reach the last index.
 *
 * For example:
 * A = [2,3,1,1,4], return true.
 *
 * A = [3,2,1,0,4], return false.
 */

public class Solution {
    public boolean canJump(int[] nums) {
        int maxIdx = 0, tmp;
        for (int i = 0 ; i < nums.length - 1; i++) {
            tmp = i + nums[i];
            maxIdx = (maxIdx >= i && tmp > maxIdx) ? tmp : maxIdx;
        }

        return maxIdx >= (nums.length - 1);
    }
}
