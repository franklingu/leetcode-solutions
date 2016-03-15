/**
 * Given numRows, generate the first numRows of Pascal's triangle.
 *
 * For example, given numRows = 5,
 * Return
 *
 * [
 *      [1],
 *     [1,1],
 *    [1,2,1],
 *   [1,3,3,1],
 *  [1,4,6,4,1]
 * ]
 */

public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();

        for (int i = 0; i < numRows; i++) {
            List<Integer> tmp = new ArrayList<Integer>();
            if (i == 0) {
                tmp.add(1);
                results.add(tmp);
                continue;
            }
            List<Integer> prev = results.get(i - 1);
            for (int j = 0; j <= i; j++) {
                if (j < i) {
                    if (j > 0 && j + 1 <= prev.size()) {
                        tmp.add(prev.get(j - 1) + prev.get(j));
                    } else {
                        tmp.add(prev.get(j));
                    }
                } else {
                    tmp.add(1);
                }
            }
            results.add(tmp);
        }

        return results;
    }
}
