/**
 * Rotate an array of n elements to the right by k steps.
 * 
 * For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
 * 
 * Note:
 * Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
 */

public class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        rotatePart(nums, 0, nums.length - 1);
        rotatePart(nums, 0, k -1);
        rotatePart(nums, k, nums.length - 1);
    }
    
    private void rotatePart(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[end];
            nums[end] = nums[start];
            nums[start] = temp;
            start++;
            end--;
        }
    }
}
