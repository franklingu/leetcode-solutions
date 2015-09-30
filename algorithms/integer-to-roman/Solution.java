/**
 * Given an integer, convert it to a roman numeral.
 * 
 * Input is guaranteed to be within the range from 1 to 3999.
 */

public class Solution {
    public String intToRoman(int num) {
        char[] arr = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
        StringBuilder result = new StringBuilder();
        StringBuilder sb = new StringBuilder();
        int currentPos = 0;
        int temp;
        while (num > 0) {
            temp = num % 10;
            if (temp <= 3) {
                while (temp > 0) {
                    sb.append(arr[currentPos]);
                    temp--;
                }
            } else if (temp == 4) {
                sb.append(arr[currentPos]);
                sb.append(arr[currentPos + 1]);
            } else if (temp == 9) {
                sb.append(arr[currentPos]);
                sb.append(arr[currentPos + 2]);
            } else {
                sb.append(arr[currentPos + 1]);
                while (temp > 5) {
                    sb.append(arr[currentPos]);
                    temp--;
                }
            }
            result = result.insert(0, sb.toString());
            sb.setLength(0);
            num /= 10;
            currentPos += 2;
        }
        
        return result.toString();
    }
}
