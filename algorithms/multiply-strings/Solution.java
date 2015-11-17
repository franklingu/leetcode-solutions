/**
 * Given two numbers represented as strings, return multiplication of the numbers as a string.
 * 
 * Note: The numbers can be arbitrarily large and are non-negative.
 */

public class Solution {
    public String multiply(String num1, String num2) {
        String result = "0";
        for (int i = num2.length() - 1; i >= 0; i--) {
            StringBuilder temp = new StringBuilder(multiplySingleDigit(num1, num2.charAt(i)));
            for (int j = num2.length() - 1; j > i; j--) {
                temp.append('0');
            }
            result = add(temp.toString(), result);
            // System.out.println(temp.toString());
            // System.out.println(result);
            // System.out.println();
        }
        int idx = 0;
        while (idx + 1 < result.length() && result.charAt(idx) == '0' && result.charAt(idx + 1) == '0') {
            idx++;
        }
        return result.substring(idx);
    }
    
    private String multiplySingleDigit(String num1, char ch) {
        if (ch == '0') {
            return "0";
        } else if (ch == '1') {
            return num1;
        }
        StringBuilder sb = new StringBuilder();
        int carry = 0, digit = (int)(ch - '0'), result = 0;
        for (int i = num1.length() - 1; i >= 0; i--) {
            result = (int)(num1.charAt(i) - '0') * digit + carry;
            carry = result / 10;
            result = result % 10;
            sb.insert(0, (char)('0' + result));
        }
        if (carry > 0) {
            sb.insert(0, (char)('0' + carry));
        }
        return sb.toString();
    }
    
    private String add(String num1, String num2) {
        StringBuilder sb = new StringBuilder();
        int carry = 0, result = 0, idx = 0;
        while (idx < num1.length() && idx < num2.length()) {
            result = (num1.charAt(num1.length() - 1 - idx) - '0') + (num2.charAt(num2.length() - 1 - idx) - '0') + carry;
            carry = result / 10;
            result = result % 10;
            sb.insert(0, (char)('0' + result));
            idx++;
        }
        while (idx < num1.length()) {
            result = (num1.charAt(num1.length() - 1 - idx) - '0') + carry;
            carry = result / 10;
            result = result % 10;
            sb.insert(0, (char)('0' + result));
            idx++;
        }
        while (idx < num2.length()) {
            result = (num2.charAt(num2.length() - 1 - idx) - '0') + carry;
            carry = result / 10;
            result = result % 10;
            sb.insert(0, (char)('0' + result));
            idx++;
        }
        if (carry > 0) {
            sb.insert(0, (char)('0' + carry));
        }
        
        return sb.toString();
    }
}
