/**
 * Reverse digits of an integer.
 * 
 * Example1: x = 123, return 321
 * Example2: x = -123, return -321
 */

public class Solution {
    public int reverse(int x) {
        boolean isNegative = (x < 0);
        x = isNegative ? (0 - x) : x;
        int[] arr = convertIntToArr(x);
        int result = convertReverseArrToInt(arr);
        return isNegative ? (0 - result) : result;
    }
    
    private int[] convertIntToArr(int x) {
        ArrayList<Integer> results = new ArrayList<Integer>();
        while (x > 0) {
            results.add(x % 10);
            x = x / 10;
        }
        int[] arr = new int[results.size()];
        for (int i = 0; i < results.size(); i++) {
            arr[i] = results.get(i);
        }
        return arr;
    }
    
    private int convertReverseArrToInt(int[] arr) {
        int sum = 0;
        int temp = sum;
        for (int i = 0; i < arr.length; i++) {
            temp = sum;
            sum = sum * 10 + arr[i];
            if (sum / 10 < temp) {  // handling of overflow case
                return 0;
            }
        }
        return sum;
    }
}
