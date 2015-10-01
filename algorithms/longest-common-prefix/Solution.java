/**
 * Write a function to find the longest common prefix string amongst an array of strings.
 */

public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length <= 0) {
            return "";
        } else if (strs.length == 1) {
            return strs[0];
        }
        StringBuilder sb = new StringBuilder();
        int currPos = 0;
        char currChar = 'a';
        while (true) {
            if (strs[0].length() > currPos) {
                currChar = strs[0].charAt(currPos);
            } else {
                break;
            }
            for (int i = 0; i < strs.length; i++) {
                if (strs[i].length() > currPos &&  strs[i].charAt(currPos) == currChar) {
                    continue;
                } else {
                    return sb.toString();
                }
            }
            sb.append(currChar);
            currPos++;
        }
        
        return sb.toString();
    }
}
