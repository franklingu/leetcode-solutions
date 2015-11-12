/**
 * Given an array of integers, every element appears three times except for one. Find that single one.
 * Note:
 * Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
 */

public class Solution {
    public int singleNumber(int[] nums) {
        int[] mapping = new int[32];
        for (int i = 0; i < nums.length; i++) {
            int temp = nums[i], counter = 31;
            while (counter >= 0) {
                mapping[counter] += (temp >> counter) & 1;
                counter--;
            }
        }
        int target = 0;
        for (int i = 0; i < 32; i++) {
            target += (1 & (mapping[i] % 3)) << i;
        }
        
        return target;
    }
}
