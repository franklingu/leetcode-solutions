/**
 * Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 * 
 * For example, given n = 3, a solution set is:
 * 
 * "((()))", "(()())", "(())()", "()(())", "()()()"
 */

public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<String>();
        if (n < 1) {
            return result;
        }
        List<StringBuilder> temp = new ArrayList<StringBuilder>();
        temp.add(new StringBuilder());
        int curr = 1;
        while (curr <= n * 2) {
            int N = temp.size();
            for (int j = 0; j < N; j++) {
                int sum = 0, open = 0;
                StringBuilder sb = temp.get(j);
                for (int i = 0; i < sb.length(); i++) {
                    if (sb.charAt(i) == '(') {
                        sum++;
                        open++;
                    } else {
                        sum--;
                    }
                }
                if (sum > 0 && open < n) {
                    StringBuilder sb1 = new StringBuilder(sb);
                    sb1.append(')');
                    temp.add(sb1);
                    sb.append('(');
                } else if (sum > 0 && open >= n) {
                    sb.append(')');
                } else if (sum == 0) {
                    sb.append('(');
                }
            }
            for (StringBuilder sb: temp) {
                System.out.format("'%s' ", sb.toString());
            }
            System.out.println();
            curr++;
        }
        for (StringBuilder sb : temp) {
            result.add(sb.toString());
        }
        return result;
    }
}
