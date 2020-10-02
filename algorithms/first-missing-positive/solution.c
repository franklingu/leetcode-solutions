//Problem Link : https://leetcode.com/problems/first-missing-positive/

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] < 1)
            {
                continue;
            }
            if (((i == 0) or (i > 0 and nums[i-1] < 1)) and nums[i] != 1)
            {
                return 1;
            }
            if (i > 0 and nums[i-1] > 0 and (nums[i] - nums[i-1] != 1 and nums[i] != nums[i-1]))
            {
                return nums[i-1]+1;
            }
        }
        
        return (nums.empty() or nums.back() < 1) ? 1 : (nums.back()+1);
    }
};
