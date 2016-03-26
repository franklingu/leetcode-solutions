/**
 * Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
 *
 * For example,
 * "A man, a plan, a canal: Panama" is a palindrome.
 * "race a car" is not a palindrome.
 *
 * Note:
 * Have you consider that the string might be empty? This is a good question to ask during an interview.
 *
 * For the purpose of this problem, we define empty string as valid palindrome.
 */

public class Solution {
    public boolean isPalindrome(String s) {
        String t = s.toLowerCase();
        int start = 0, end = t.length() - 1;
        while (start < end) {
            if (isAlphanumeric(t.charAt(start)) && isAlphanumeric(t.charAt(end))) {
                if (t.charAt(start) != t.charAt(end)) {
                    return false;
                }
                start++;
                end--;
            } else if (isAlphanumeric(t.charAt(start))) {
                end--;
            } else if (isAlphanumeric(t.charAt(end))) {
                start++;
            } else {
                start++;
                end--;
            }
        }
        return true;
    }

    private boolean isAlphanumeric(char c) {
        return (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9');
    }
}
