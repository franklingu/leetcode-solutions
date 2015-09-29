/**
 * Determine whether an integer is a palindrome. Do this without extra space.
 */

public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int x_t = x;
        int digits = 0;
        while (x_t > 0) {
            x_t /= 10;
            digits++;
        }
        int num1, num2;
        for (int i = 0, j = digits - 1; i < j; i++, j--) {
            num1 = x / tensPower(i) % 10;
            num2 = x / tensPower(j) % 10;
            if (num1 == num2) {
                continue;
            } else {
                return false;
            }
        }
        return true;
    }
    
    private int tensPower(int n) {
        int sum = 1;
        while (n > 0) {
            sum *= 10;
            n--;
        }
        return sum;
    }
}
