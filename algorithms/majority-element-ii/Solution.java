/**
 * Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
 * The algorithm should run in linear time and in O(1) space.
 */

public class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Integer num1 = null, num2 = null;
        int count1 = 0, count2 = 0;
        
        for (int i = 0; i < nums.length; i++) {
            if (num1 != null && nums[i] == num1.intValue()) {
                count1++;
            } else if (num2 != null && nums[i] == num2.intValue()) {
                count2++;
            } else if (count1 == 0) {
                num1 = nums[i];
                count1 = 1;
            } else if (count2 == 0) {
                num2 = nums[i];
                count2 = 1;
            } else {
                count1--;
                count2--;
            }
        }
        count1 = 0;
        count2 = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == num1.intValue()) {
                count1++;
            } else if (nums[i] == num2.intValue()) {
                count2++;
            }
        }
        
        List<Integer> results = new ArrayList<Integer>();
        if (count1 > nums.length / 3) {
            results.add(num1);
        }
        if (count2 > nums.length / 3) {
            results.add(num2);
        }
        
        return results;
    }
}
