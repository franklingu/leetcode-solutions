/**
 * Given an array of integers and an integer k, find out whether there are two
 * distinct indices i and j in the array such that nums[i] = nums[j] and the
 *difference between i and j is at most k.
 */

public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> st = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (st.containsKey(nums[i]) && i - st.get(nums[i]).intValue() <= k) {
                return true;
            }
            st.put(nums[i], i);
        }
        return false;
    }
}
