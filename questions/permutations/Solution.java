/**
 * Given a collection of numbers, return all possible permutations.
 * 
 * For example,
 * [1,2,3] have the following permutations:
 * [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
 */

public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        return permutations(nums, nums.length - 1);
    }
    
    private List<List<Integer>> permutations(int[] nums, int k) {
        if (k == 0) {
            List<List<Integer>> temps = new LinkedList<List<Integer>>();
            List<Integer> t = new LinkedList<Integer>();
            t.add(nums[0]);
            temps.add(t);
            return temps;
        }
        List<List<Integer>> temps = permutations(nums, k - 1);
        List<List<Integer>> results = new LinkedList<List<Integer>>();
        for (List<Integer> l : temps) {
            for (int i = 0; i <= l.size(); i++) {
                List<Integer> t = new LinkedList<Integer>(l);
                t.add(i, nums[k]);
                results.add(t);
            }
        }
        return results;
    }
}
