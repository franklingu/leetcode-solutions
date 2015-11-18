/**
 * Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
 * 
 * The same repeated number may be chosen from C unlimited number of times.
 * 
 * Note:
 * All numbers (including target) will be positive integers.
 * The solution set must not contain duplicate combinations.
 * For example, given candidate set 2,3,6,7 and target 7, 
 * A solution set is: 
 * [7] 
 * [2, 2, 3] 
 */

public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        Map<Integer, List<List<Integer>>> mapping = new HashMap<Integer, List<List<Integer>>>();
        return findCombinationSum(candidates, target, mapping);
    }
    
    private List<List<Integer>> findCombinationSum(int[] candidates, int target, Map<Integer, List<List<Integer>>> mapping) {
        if (mapping.containsValue(target)) {
            return mapping.get(target);
        }
        int diff;
        List<Integer> elems;
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        List<List<Integer>> temp;
        for (int i = 0; i < candidates.length; i++) {
            if (target < candidates[i]) {
                break;
            }
            diff = target - candidates[i];
            if (diff == 0) {
                elems = new ArrayList<Integer>();
                elems.add(candidates[i]);
                results.add(elems);
            } else {
                temp = findCombinationSum(candidates, diff, mapping);
                for (List<Integer> l : temp) {
                    if (l.size() > 0 && l.get(l.size() - 1) <= candidates[i]) {
                        elems = new ArrayList<Integer>(l);
                        elems.add(candidates[i]);
                        results.add(elems);
                    }
                }
            }
        }
        mapping.put(target, results);
        return results;
    }
}
