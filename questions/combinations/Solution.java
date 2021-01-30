/**
 * Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
 * 
 * For example,
 * If n = 4 and k = 2, a solution is:
 * 
 * [
 *   [2,4],
 *   [3,4],
 *   [2,3],
 *   [1,2],
 *   [1,3],
 *   [1,4],
 * ]
 */

public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        if (k <= 0) {
            return new ArrayList<List<Integer>>();
        }
        if (k == 1) {
            List<List<Integer>> temps = new ArrayList<List<Integer>>();
            for (int i = 1; i <= n; i++) {
                List<Integer> t = new ArrayList<Integer>();
                t.add(i);
                temps.add(t);
            }
            return temps;
        }
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        List<List<Integer>> temps = combine(n, k - 1);
        for (List<Integer> l : temps) {
            for (int i = 1; i <= n; i++) {
                if (l.size() > 0 && l.get(l.size() - 1) < i) {
                    List<Integer> t = new ArrayList<Integer>(l);
                    t.add(i);
                    results.add(t);
                }
            }
        }
        
        return results;
    }
}
