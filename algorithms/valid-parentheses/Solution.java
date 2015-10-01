/**
 * Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string
 * is valid.
 * 
 * The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
 */

public class Solution {
    public boolean isValid(String s) {
        char[] arr = {'(', ')', '{', '}', '[', ']'};
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < s.length(); i++) {
            if (sb.length() > 0) {
                char temp = peekChar(sb);
                if (areTwoMatching(temp, s.charAt(i), arr)) {
                    popChar(sb);
                } else {
                    pushChar(sb, s.charAt(i));
                }
            } else {
                pushChar(sb, s.charAt(i));
            }
        }
        
        return sb.length() == 0;
    }
    
    private void pushChar(StringBuilder sb, char c) {
        sb.append(c);
    }
    
    private char popChar(StringBuilder sb) {
        char temp = sb.charAt(sb.length() - 1);
        sb.setLength(sb.length() - 1);
        return temp;
    }
    
    private char peekChar(StringBuilder sb) {
        return sb.charAt(sb.length() - 1);
    }
    
    private boolean areTwoMatching(char l, char r, char[] arr) {
        int numl = -1;
        int numr = -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == l) {
                numl = i;
            }
            if (arr[i] == r) {
                numr = i;
            }
        }
        return (numl != -1 && numr != -1 && numl < numr && (numl >> 1) == (numr >> 1));
    }
}
