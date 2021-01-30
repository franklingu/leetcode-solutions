/**
 * Given a non negative integer number num. For every numbers i in the range
 * 0 ≤ i ≤ num calculate the number of 1's in their binary representation and
 * return them as an array.
 *
 * Example:
 * For num = 5 you should return [0,1,1,2,1,2].
 *
 * Follow up:
 *
 * It is very easy to come up with a solution with run time O(n*sizeof(integer)).
 * But can you do it in linear time O(n) /possibly in a single pass?
 * Space complexity should be O(n).
 * Can you do it like a boss? Do it without using any builtin function like
 * __builtin_popcount in c++ or in any other language.
 */

public class Solution {
    public int[] countBits(int num) {
        int[] results = new int[num + 1];
        if (num == 0) {
            results[0] = 0;
            return results;
        } else if (num == 1) {
            results[0] = 0;
            results[1] = 1;
            return results;
        } else {
            results[0] = 0;
            results[1] = 1;
        }
        int sz = 2, runner = 0;
        while (sz + runner <= num) {
            if (runner < sz) {
                results[sz + runner] = results[runner] + 1;
                runner++;
            } else {
                sz = sz << 1;
                runner = 0;
                results[sz + runner] = results[runner] + 1;
                runner++;
            }
        }

        return results;
    }
}
