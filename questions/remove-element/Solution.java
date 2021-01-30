/**
 * Given an array and a value, remove all instances of that value in place and return the new length.
 * 
 * The order of elements can be changed. It doesn't matter what you leave beyond the new length.
 */

public class Solution {
    public int removeElement(int[] nums, int val) {
        if (nums == null) {
            return 0;
        }
        int curr = 0;
        int runner = 0;
        while (runner < nums.length) {
            if (nums[runner] != val) {
                nums[curr] = nums[runner];
                curr++;
            }
            runner++;
        }
        
        return curr;
    }
}
