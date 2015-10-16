import java.lang.Math;
import java.util.HashMap;
import java.util.Map;

/**
 * Given a positive integer n, find the least number of perfect
 * square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
 *
 * For example, given n = 12, return 3 because 12 = 4 + 4 + 4;
 * given n = 13, return 2 because 13 = 4 + 9.
 *
 */
public class Solution {
    private Map<Integer, Integer> minNums = new HashMap<Integer, Integer>();
    
    public int numSquares(int n) {
        if (minNums.containsKey(n)) { return minNums.get(n); }
        
        int sqrt = (int) Math.sqrt(n);
        int newVal = sqrt*sqrt;
        if (newVal == n) {
            minNums.put(n, 1);
            return 1;
        }
        
        int currentMin = Integer.MAX_VALUE;
        while(sqrt > 0) {
            int newMin = numSquares(n-newVal);
            
            if (newMin + 1 < currentMin) {
                currentMin = newMin + 1;
            }
            
            newVal -= (2*sqrt - 1);
            sqrt -= 1;
        }
        
        minNums.put(n, currentMin);
        
        return currentMin;
    }
}