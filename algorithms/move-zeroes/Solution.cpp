/**
 * Given an array nums, write a function to move all 0's to the end of it 
 * while maintaining the relative order of the non-zero elements.
 * 
 * For example, given nums = [0, 1, 0, 3, 12], after calling your 
 * function, nums should be [1, 3, 12, 0, 0].
 *
 * Note:
 * You must do this in-place without making a copy of the array.
 * Minimize the total number of operations.
 *
 */
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // keeps track of the start of the string of zeroes
        // or current element being checked (initial value)
        int startIndex = 0;
        
        for (int i = 0 ; i < nums.size() ; i ++) {
            // if we meet a non-zero element and 
            // if we have already found zeroes
            if (nums[i] != 0 && startIndex != i) {
                // swap the location of the start of 
                // the string of zeroes with the new 
                // non-zero value
                int temp = nums[i];
                nums[i] = nums[startIndex];
                nums[startIndex] = temp;
            }
            
            // if we have swapped or if we have not
            // found any zeroes yet, increment
            // the startIndex
            if (nums[startIndex] != 0) {
                startIndex ++;
            }
        }
    }
};