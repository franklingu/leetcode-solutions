/**
 * Given a pattern and a string str, find if str follows the same pattern.
 * 
 * Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty
 * word in str.
 * 
 * Examples:
 * pattern = "abba", str = "dog cat cat dog" should return true.
 * pattern = "abba", str = "dog cat cat fish" should return false.
 * pattern = "aaaa", str = "dog cat cat dog" should return false.
 * pattern = "abba", str = "dog dog dog dog" should return false.
 * Notes:
 * You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a
 * single space.
 */

public class Solution {
    public boolean wordPattern(String pattern, String str) {
        String[] splits = str.split(" ");
        if (splits.length != pattern.length()) {
            return false;
        }
        
        for (int i = 0; i < pattern.length(); i++) {
            for (int j = i + 1; j < pattern.length(); j++) {
                if (pattern.charAt(i) != pattern.charAt(j)) {
                    if (splits[i].equals(splits[j])) {
                        return false;
                    }
                } else {
                    if (!splits[i].equals(splits[j])) {
                        return false;
                    }
                }
            }
        }
        
        return true;
    }
}
