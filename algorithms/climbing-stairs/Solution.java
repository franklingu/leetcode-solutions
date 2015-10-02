/**
 * You are climbing a stair case. It takes n steps to reach to the top.
 * 
 * Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 */

public class Solution {
    public int climbStairs(int n) {
        if (n <= 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        }
        int[] arr = new int[n];
        arr[0] = 1;
        return countWays(n, arr);
    }
    
    private int countWays(int n, int[] arr) {
        if (n < 0) {
            return -1;
        } else if (n == 0) {
            return 1;
        }
        if (arr[n - 1] != 0) {
            return arr[n - 1];
        }
        int result1 = countWays(n - 1, arr), result2 = countWays(n - 2, arr);
        arr[n - 1] = result1 + result2;
        
        return arr[n - 1];
    }
}
