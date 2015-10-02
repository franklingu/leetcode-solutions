/**
 * Given two binary strings, return their sum (also a binary string).
 * 
 * For example,
 * a = "11"
 * b = "1"
 * Return "100".
 */

public class Solution {
    public String addBinary(String a, String b) {
        if (a == null && b == null) {
            return null;
        } else if (a == null) {
            return b;
        } else if (b == null) {
            return a;
        }
        StringBuilder sb = new StringBuilder();
        int runner = 0;
        int carry = 0;
        int result = 0;
        while (runner < a.length() && runner < b.length()) {
            result = carry + (a.charAt(a.length() - 1 - runner) - '0') + (b.charAt(b.length() - 1 - runner) - '0');
            carry = result / 2;
            result = result % 2;
            if (result == 0) {
                sb.insert(0, '0');
            } else {
                sb.insert(0, '1');
            }
            runner++;
        }
        String remaining;
        if (runner >= a.length()) {
            remaining = b;
        } else {
            remaining = a;
        }
        while (runner < remaining.length()) {
            result = carry + (remaining.charAt(remaining.length() - 1 - runner) - '0');
            carry = result / 2;
            result = result % 2;
            if (result == 0) {
                sb.insert(0, '0');
            } else {
                sb.insert(0, '1');
            }
            runner++;
        }
        if (carry == 1) {
            sb.insert(0, '1');
        }
        
        return sb.toString();
    }
}
