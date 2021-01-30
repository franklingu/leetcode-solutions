/**
 * Given an index k, return the kth row of the Pascal's triangle.
 *
 * For example, given k = 3,
 * Return [1,3,3,1].
 *
 * Note:
 * Could you optimize your algorithm to use only O(k) extra space?
 */

public class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> results = new LinkedList<Integer>();
        if (rowIndex == 0) {
            results.add(1);
            return results;
        } else if (rowIndex == 1) {
            results.add(1);
            results.add(1);
            return results;
        }
        results.add(1);
        results.add(1);
        int prev = 1, tmp = 0;
        for (int i = 1; i < rowIndex; i++) {
            prev = 1;
            for (int j = 1; j <= i; j++) {
                tmp = results.get(j);
                results.set(j, tmp + prev);
                prev = tmp;
            }
            results.add(1);
        }

        return results;
    }
}
