//Problem Link : https://leetcode.com/problems/first-missing-positive/

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int it = 1;
        for(int itr=0;i<nums.size();itr++){
            if(nums[itr]>0){
                if(nums[itr]==it)
                    it++;
                else if(nums[itr]>it)
                    return it;
            }
        }
        
        return it;
        
    }
};
