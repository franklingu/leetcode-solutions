/**
 * Write a program to find the n-th ugly number.
 * 
 * Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9,
 * 10, 12 is the sequence of the first 10 ugly numbers.
 * 
 * Note that 1 is typically treated as an ugly number.
 */

public class Solution {
    public int nthUglyNumber(int n) {
        ArrayList<Integer> results = new ArrayList<Integer>();
        results.add(1);
        int num1, num2, num3, num;
        int id1 = 0, id2 = 0, id3 = 0;
        
        while (results.size() < n) {
            num1 = results.get(id1) * 2;
            num2 = results.get(id2) * 3;
            num3 = results.get(id3) * 5;
            num = Math.min(Math.min(num1, num2), num3);
            if (num == num1) {
                id1++;
            } 
            if (num == num2) {
                id2++;
            }
            if (num == num3) {
                id3++;
            }
            results.add(num);
        }
        
        return results.get(results.size() - 1);
    }
}
