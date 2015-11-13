/**
 * Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
 * 
 * For example,
 * Given nums = [0, 1, 3] return 2.
 * 
 * Note:
 * Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
 */

public class Solution {
    public int missingNumber(int[] nums) {
        int sum = 0;
        for (int i = nums.length - 1; i >= 0; i--) {
            sum += nums[i];
        }
        
        return (nums.length + 1) * nums.length / 2 - sum; 
    }
}
