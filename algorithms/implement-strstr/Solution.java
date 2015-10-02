/**
 * Implement strStr().
 *
 * Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 */

public class Solution {
    /**
     * A more efficient implementation could be found
     *   https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
     */
    public int strStr(String haystack, String needle) {
        int runner = 0;
        boolean found = false;
        boolean matching = true;
        while (needle.length() + runner <= haystack.length()) {
            matching = true;
            for (int i = 0; i < needle.length(); i++) {
                if (needle.charAt(i) != haystack.charAt(i + runner)) {
                    matching = false;
                    break;
                }
            }
            if (matching) {
                found = true;
                break;
            }
            runner++;
        }
        
        return found ? runner : -1;
    }
}
