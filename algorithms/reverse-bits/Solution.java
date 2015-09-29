/**
 * Reverse bits of a given 32 bits unsigned integer.
 * 
 * For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
 * return 964176192 (represented in binary as 00111001011110000010100101000000).
 * 
 * Follow up:
 * If this function is called many times, how would you optimize it?
 */

public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int[] arr = new int[32];
        long mask = 1;
        long nL = n;
        long sum = 0;
        for (int i = 0; i < 32; i++) {
            if ((nL & mask) > 0) {
                arr[32 - 1 - i] = 1;
            }
            mask = mask << 1; 
        }
        mask = 1;
        for (int i = 0; i < 32; i++) {
            if (arr[i] == 1) {
                sum = sum | (mask << i);
            }
        }
        return (int)(sum);
    }
}
