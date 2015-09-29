/**
 * Implement atoi to convert a string to an integer.
 * 
 * Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and
 * ask yourself what are the possible input cases.
 * 
 * Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are
 * responsible to gather all the input requirements up front.
 */

public class Solution {
    public int myAtoi(String str) {
        str = str.trim();
        if (str == null || str.length() <= 0) {
            return 0;
        }
        if (!(str.charAt(0) == '-' || str.charAt(0) == '+' || (str.charAt(0) >= '0' && str.charAt(0) <= '9'))) {
            return 0;
        }
        boolean isNegative = false;
        int startIdx = 0;
        long result = 0, posLimit = 2147483647;
        if (str.charAt(0) == '-') {
            isNegative = true;
            startIdx = 1;
        } else if (str.charAt(0) == '+') {
            startIdx = 1;
        }
        
        for (int i = startIdx; i < str.length(); i++) {
            if (str.charAt(i) >= '0' && str.charAt(i) <= '9') {
                result = result * 10 + (str.charAt(i) - '0');
            } else {
                break;
            }
            if (isNegative) {
                if (result > (posLimit + 1)) {
                    result = posLimit + 1;
                }
            } else {
                if (result > posLimit) {
                    result = posLimit;
                }
            }
        }
        return isNegative ? ((int)-result) : (int)result;
    }
}
