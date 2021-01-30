/**
 * Given a non-negative number represented as an array of digits, plus one to the number.
 * 
 * The digits are stored such that the most significant digit is at the head of the list.
 */

public class Solution {
    public int[] plusOne(int[] digits) {
        if (digits == null) {
            return null;
        }
        return addOneRec(digits.clone(), 1, digits.length - 1);
    }
    
    private int[] addOneRec(int[] digits, int carry, int pos) {
        if (carry == 0) {
            return digits;
        }
        int temp = digits[pos] + carry;
        if (temp <= 9) {
            digits[pos] = temp;
            return digits;
        }
        digits[pos] = temp % 10;
        if (pos == 0) {
            int[] result = new int[digits.length + 1];
            System.arraycopy(digits, 0, result, 1, digits.length);
            result[0] = temp / 10;
            return result;
        } else {
            return addOneRec(digits, temp / 10, pos + 1);
        }
    }
}
