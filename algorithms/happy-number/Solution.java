/**
 * Write an algorithm to determine if a number is "happy".
 * A happy number is a number defined by the following process: 
 * Starting with any positive integer, replace the number by the 
 * sum of the squares of its digits, and repeat the process until
 * the number equals 1 (where it will stay), or it loops 
 * endlessly in a cycle which does not include 1. Those numbers
 * for which this process ends in 1 are happy numbers.
 *
 * Example: 19 is a happy number
 * 12 + 92 = 82
 * 82 + 22 = 68
 * 62 + 82 = 100
 * 12 + 02 + 02 = 1
 */

public class Solution {
    public boolean isHappy(int n) {
        List<Integer> existingNumbers = new ArrayList<Integer>();
        
        while (true) {
            int nextInt = nextStep(n);
            if (nextInt == 1) {
                return true;
            } else if (existingNumbers.contains(nextInt)) {
                return false;
            }
            
            existingNumbers.add(nextInt);
            n = nextInt;
        }
    }
    
    public int nextStep(int num) {
        int answer = 0;
        while (num > 0) {
            answer += (num%10) * (num%10);
            num /= 10;
        }
        
        return answer;
    }
}