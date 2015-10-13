/**
 * Follow up for H-Index: What if the citations array is
 * sorted in ascending order? Could you optimize your algorithm?
 */

public class Solution {
    public int hIndex(int[] citations) {
        int length = citations.length;
        for (int i = 0 ; i < length ; i++) {
            if (citations[i] >= (length - i) && (i == 0 || citations[i-1] <= (length - i))) {
                return (length - i);
            }
        }
        
        return 0;
    }
}