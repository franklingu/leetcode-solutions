/**
 * Given an array of numbers nums, in which exactly two elements appear only once and all the other elements
 * appear exactly twice. Find the two elements that appear only once.
 * For example:
 * Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
 * 
 * Note:
 * The order of the result is not important. So in the above example, [5, 3] is also correct.
 * Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
 */

public class Solution {
    public int[] singleNumber(int[] nums) {
        int distinguisher = 0;
        for (int i = 0; i < nums.length; i++) {
            distinguisher = distinguisher ^ nums[i];
        }
        distinguisher = ((distinguisher - 1) ^ distinguisher) & distinguisher;
        int target1 = 0, target2 = 0;
        for (int i = 0; i < nums.length; i++) {
            if ((nums[i] & distinguisher) == 0) {
                target1 = target1 ^ nums[i];
            } else {
                target2 = target2 ^ nums[i];
            }
        }
        
        return new int[]{target1, target2};
    }
}
