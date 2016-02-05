/**
 * Given a sorted positive integer array nums and an integer n, add/patch elements to the array
 * such that any number in range [1, n] inclusive can be formed by the sum of some elements in
 * the array. Return the minimum number of patches required.
 * 
 * Example 1:
 * nums = [1, 3], n = 6
 * Return 1.
 * 
 * Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
 * Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
 * Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
 * So we only need 1 patch.
 * 
 * Example 2:
 * nums = [1, 5, 10], n = 20
 * Return 2.
 * The two patches can be [2, 4].
 * 
 * Example 3:
 * nums = [1, 2, 2], n = 5
 * Return 0.
 */

public class Solution {
    public int minPatches(int[] nums, int n) {
        List<Integer> sums = new ArrayList<Integer>();
        
        // generate all the possible sums
        for (int i : nums) {
            addNumToSums(sums,i,n);
        }
        
        int min = 1;
        int answer = 0;
        
        // find the min number missing in the sums
        for(;sums.contains(min);min++);
        while(min <= n) {
            answer ++;
            // add the min number to sums
            addNumToSums(sums, min, n);
            
            // find the next min number
            for(;sums.contains(min);min++);
        }
        
        return answer;
    }
    
    /**
     * adds the given number to the sums array. also adds
     * combination of the given number and existing
     * numbers in the array. 
     * 
     * @param n is the max value that is added to the array
     * 
     */
    public void addNumToSums(List<Integer> sums, int i, int n) {
        // if given value is more than n, ignore
        if (i <= n) {
            List<Integer> temp = new ArrayList<Integer>();
            
            // add i to the list
            temp.add(i);
            for (int j : sums) {
                
                // if the current combined sum is more than n, ignore
                if (i+j <= n) {
                    temp.add(i+j);
                }
            }
            
            sums.addAll(temp);
            temp.clear();
        }
    }
}