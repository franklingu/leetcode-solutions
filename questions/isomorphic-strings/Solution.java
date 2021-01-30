/**
 * Given two strings s and t, determine if they are isomorphic.
 * Two strings are isomorphic if the characters in s can be replaced to get t.
 * All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
 * For example,
 * Given "egg", "add", return true.
 * Given "foo", "bar", return false.
 * Given "paper", "title", return true.
 * Note:
 * You may assume both s and t have the same length.
 */

public class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Character> mapping = new HashMap<Character, Character>();
        for (int i = 0; i < s.length(); i++) {
            if (mapping.containsKey(s.charAt(i))) {
                if (mapping.get(s.charAt(i)).charValue() != t.charAt(i)) {
                    return false;
                }
            } else {
                mapping.put(s.charAt(i), t.charAt(i));
            }
        }
        HashSet<Character> valSet = new HashSet<Character>();
        for (Character c : mapping.values()) {
            if (valSet.contains(c)) {
                return false;
            }
            valSet.add(c);
        }
        
        return true;
    }
}
