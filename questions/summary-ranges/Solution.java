/**
 * Given a sorted integer array without duplicates, return the summary of its ranges.
 * 
 * For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
 */

public class Solution {
    public List<String> summaryRanges(int[] nums) {
        if (nums == null || nums.length <= 0) {
            return new ArrayList<String>();
        }
        int start = nums[0], curr = start;
        List<String> results = new ArrayList<String>();
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == curr + 1) {
                curr++;
                continue;
            } else if (nums[i] > curr + 1) {
                if (curr == start) {
                    results.add("" + start);
                } else {
                    results.add("" + start + "->" + curr);
                }
                start = nums[i];
                curr = start;
            }
        }
        if (curr == start) {
            results.add("" + start);
        } else {
            results.add("" + start + "->" + curr);
        }
        
        return results;
    }
}
