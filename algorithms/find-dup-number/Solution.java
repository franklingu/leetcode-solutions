/**
 * Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive)
 * Assume that there is only one duplicate number, find the duplicate one.
 * O(1) extra space. Smaller than O(n^2) time complexcity.
 * Input: [2,1,2]
 * Output: 2
 */

public class Solution {
    public int findDuplicate(int[] nums) {
        int btm=1, top=nums.length-1;
        while(btm != top){
            int bigger_count=0, smaller_count=0;
            int mid=(btm+top)/2;
            last_length=cur_length;
            for(int i=1; i<=nums.length-1; i++){
                if(nums[i] > mid && nums[i] <= top) bigger_count++;
                else if(nums[i] <= mid && nums[i] >= btm) smaller_count++;
            }
            if(bigger_count > smaller_count){
                btm=mid+1;
            }
            else{
                top=mid;
            }
        }
        return btm;
    }
    
}
