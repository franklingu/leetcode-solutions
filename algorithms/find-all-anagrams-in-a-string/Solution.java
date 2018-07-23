/**
 * Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
 *
 * Strings consists of lowercase English letters only and the length
 * of both strings s and p will not be larger than 20,100.
 *
 * The order of output does not matter.
 *
 * Example 1:
 *
 * Input:
 * s: "cbaebabacd" p: "abc"
 *
 * Output:
 * [0, 6]
 *
 * Explanation:
 * The substring with start index = 0 is "cba", which is an anagram of "abc".
 * The substring with start index = 6 is "bac", which is an anagram of "abc".
 *
 * Input:
 * s: "abab" p: "ab"
 *
 * Output:
 * [0, 1, 2]
 *
 * Explanation:
 * The substring with start index = 0 is "ab", which is an anagram of "ab".
 * The substring with start index = 1 is "ba", which is an anagram of "ab".
 * The substring with start index = 2 is "ab", which is an anagram of "ab".
 */
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int ls = s.length(), lp = p.length();
        int start = 0, end = ls - lp + 1;
        List<Integer> ret = new ArrayList();
        if (ls < lp) {
            return ret;
        }

        HashMap<Character, Integer> track = new HashMap<Character, Integer>();
        for (int i = 0; i < lp; i++) {
            char c = p.charAt(i);
            if (track.containsKey(c)) {
                track.put(c, track.get(c) + 1);
            } else {
                track.put(c, 1);
            }
            c = s.charAt(i);
            if (track.containsKey(c)) {
                track.put(c, track.get(c) - 1);
            } else {
                track.put(c, -1);
            }
        }

        while (start < end) {
            boolean isAna = true;
            for (Integer val : track.values()) {
                if (val != 0) {
                    isAna = false;
                    break;
                }
            }
            if (isAna) {
                ret.add(start);
            }
            if (start + lp < ls) {
                char c = s.charAt(start);
                track.put(c, track.get(c) + 1);
                // System.out.print(c);
                c = s.charAt(start + lp);
                if (track.containsKey(c)) {
                    track.put(c, track.get(c) - 1);
                } else {
                    track.put(c, -1);
                }
            }
            start++;
        }

        return ret;
    }
}
