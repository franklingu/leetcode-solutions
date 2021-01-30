/**
 * Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than
 * 2^31 - 1.
 * 
 * For example,
 * 123 -> "One Hundred Twenty Three"
 * 12345 -> "Twelve Thousand Three Hundred Forty Five"
 * 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 */

public class Solution {
    public String numberToWords(int num) {
        if (num == 0) {
            return "Zero";
        }
        LinkedList<Integer> results = new LinkedList<Integer>();
        String[] mapping1 = new String[]{"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        String[] mapping2 = new String[]{"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
        String[] mapping3 = new String[]{"", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
        String[] digits = new String[]{"", "Thousand", "Million", "Billion"};
        while (num > 0) {
            results.offer(num % 10);
            num = num / 10;
        }
        StringBuilder fsb = new StringBuilder();
        StringBuilder sb = new StringBuilder();
        int val1, val2, val3, counter = 0;
        while (!results.isEmpty()) {
            if (results.size() <= 1) {
                val1 = results.poll();
                val2 = 0;
                val3 = 0;
            } else if (results.size() <= 2) {
                val1 = results.poll();
                val2 = results.poll();
                val3 = 0;
            } else {
                val1 = results.poll();
                val2 = results.poll();
                val3 = results.poll();
            }
            if (val3 != 0) {
                sb.append(mapping1[val3] + " Hundred ");
            }
            if (val2 != 0 && val2 != 1) {
                sb.append(mapping3[val2] + " ");
            }
            if (val2 == 1) {
                sb.append(mapping2[val1] + " ");
            } else {
                if (val1 != 0) {
                    sb.append(mapping1[val1] + " ");
                }
            }
            if (counter != 0 && (val1 != 0 || val2 != 0 || val3 != 0)) {
                sb.append(digits[counter] + " ");
            }
            counter++;
            fsb.insert(0, sb.toString());
            sb = new StringBuilder();
        }
        
        return fsb.toString().trim();
    }
}
