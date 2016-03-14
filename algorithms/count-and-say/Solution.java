/**
 * The count-and-say sequence is the sequence of integers beginning as follows:
 * 1, 11, 21, 1211, 111221, ...
 *
 * 1 is read off as "one 1" or 11.
 * 11 is read off as "two 1s" or 21.
 * 21 is read off as "one 2, then one 1" or 1211.
 * Given an integer n, generate the nth sequence.
 *
 * Note: The sequence of integers will be represented as a string.
 */

public class Solution {
    public String countAndSay(int n) {
        if (n == 1) {
            return "1";
        }
        String result = "1";
        for (int i = 1; i < n; i++) {
            result = convert(result);
            System.out.println(result);
        }
        return result;
    }

    private String convert(String input) {
        StringBuilder sb = new StringBuilder();
        char prev = '1';
        int count = 0;
        for (int i = 0; i < input.length(); i++) {
            if (i == 0) {
                prev = input.charAt(i);
                count++;
            } else {
                if (input.charAt(i) == prev) {
                    count++;
                } else {
                    sb.append((char)(count + (int)'0'));
                    sb.append(prev);
                    count = 1;
                    prev = input.charAt(i);
                }
            }
        }
        sb.append((char)(count + (int)'0'));
        sb.append(prev);
        return sb.toString();
    }
}
