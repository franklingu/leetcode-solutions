/**
 * Given a roman numeral, convert it to an integer.
 * 
 * Input is guaranteed to be within the range from 1 to 3999.
 */

public class Solution {
    public int romanToInt(String s) {
        char[] arr = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
        int[] mapped = {1, 5, 10, 50, 100, 500, 1000};
        int sum = 0;
        int currPos = 0;
        int prevPos = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            currPos = indexOfTarget(arr, s.charAt(i));
            if (currPos < prevPos) {
                sum -= mapped[currPos];
            } else {
                sum += mapped[currPos];
            }
            prevPos = currPos;
        }
        
        return sum;
    }
    
    private int indexOfTarget(char[] arr, char target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }
}
