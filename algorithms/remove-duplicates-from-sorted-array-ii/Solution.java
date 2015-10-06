/**
 * Follow up for "Remove Duplicates":
 * What if duplicates are allowed at most twice?
 * 
 * For example,
 *   Given sorted array nums = [1,1,1,2,2,3],
 *   Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
 *   It doesn't matter what you leave beyond the new length.
 */

public class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums == null || nums.length <= 0) {
            return 0;
        }
        int acc = 1;
        int runner = 1;
        int curr = 1;
        while (runner < nums.length) {
            if (nums[runner] == nums[runner - 1]) {
                acc++;
                if (acc <= 2) {
                    nums[curr] = nums[runner];
                    curr++;
                }
            } else {
                nums[curr] = nums[runner];
                curr++;
                acc = 1;
            }
            runner++;
        }
        return curr;
    }
}
