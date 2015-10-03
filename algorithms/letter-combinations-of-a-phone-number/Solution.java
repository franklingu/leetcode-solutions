/**
 * Given a digit string, return all possible letter combinations that the number could represent.
 * 
 * A mapping of digit to letters (just like on the telephone buttons) is given below.
 * 0: " ", 1: null, 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
 *
 * Input:Digit string "23"
 * Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 */

public class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> results = new ArrayList<String>();
        if (digits == null || digits.length() <= 0 || digits.indexOf('1') != -1) {
            return results;
        }
        String[] map = {" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        List<String> temp = new ArrayList<String>();
        temp.add("");
        for (int i = 0; i < digits.length(); i++) {
            String mapped = map[digits.charAt(i) - '0'];
            int N = temp.size();
            List<String> temp1 = new ArrayList<String>();
            for (int k = 0; k < mapped.length(); k++) {
                for (int j = 0; j < N; j++) {
                    temp1.add(temp.get(j) + mapped.substring(k, k + 1));
                }
            }
            temp = temp1;
        }
        results = temp;
        
        return results;
    }
}
