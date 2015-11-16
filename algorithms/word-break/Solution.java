/**
 * Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated
 * sequence of one or more dictionary words.
 * 
 * For example, given
 * s = "leetcode",
 * dict = ["leet", "code"].
 * 
 * Return true because "leetcode" can be segmented as "leet code".
 */

public class Solution {
    public boolean wordBreak(String s, Set<String> wordDict) {
        boolean[] matches = new boolean[s.length() + 1];
        matches[0] = true;
        
        for (int i = 0; i < s.length(); i++) {
            if (!matches[i]) {
                continue;
            }
            for (String word : wordDict) {
                int end = i + word.length();
                if (end > s.length()) {
                    continue;
                }
                if (matches[end]) {
                    continue;
                }
                if (s.substring(i, end).equals(word)) {
                    matches[end] = true;
                }
            }
        }
        
        return matches[s.length()];
    }
}
