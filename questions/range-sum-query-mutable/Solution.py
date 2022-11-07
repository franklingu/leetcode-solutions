"""

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

 
Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

 
Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.


"""


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.seg_tree = [dict() for _ in range(4*self.n)]
        
        def build(i, j, indx):
            self.seg_tree[indx]['left'] = i
            self.seg_tree[indx]['right'] = j
            
            if i == j:
                self.seg_tree[indx]['val'] = nums[i]
                return
            
            mid = (i+j)//2
            
            build(i, mid, 2*indx)
            build(mid+1, j, 2*indx+1)
            
            self.seg_tree[indx]['val'] =  self.seg_tree[2*indx]['val'] +self.seg_tree[2*indx+1]['val']
        
        build(0,self.n-1,1) # start the tree from index 1
        
        
                
    def update(self, index: int, val: int) -> None:
        
        def seg_update(index, val, indx):
            i = self.seg_tree[indx]['left']
            j = self.seg_tree[indx]['right']
            
            if i==j and i==index:
                self.seg_tree[indx]['val'] = val
                return
            
            mid = (i+j)//2
            
            if index<=mid:
                seg_update(index,val,2*indx)
                self.seg_tree[indx]['val'] =  self.seg_tree[2*indx]['val'] +self.seg_tree[2*indx+1]['val']
            else:
                seg_update(index,val,2*indx+1)
                self.seg_tree[indx]['val'] =  self.seg_tree[2*indx]['val'] +self.seg_tree[2*indx+1]['val']
        
        seg_update(index, val, 1)
        

    def sumRange(self, left: int, right: int) -> int:
        
        def query(left, right, indx):
            i = self.seg_tree[indx]['left']
            j = self.seg_tree[indx]['right']
            
            if i == left and j == right:
                return self.seg_tree[indx]['val']
            
            mid = (i+j)//2
            
            if i <= left and right <=mid:
                return query(left,right,2*indx)
            if mid+1<=left and right <= j:
                return query(left,right,2*indx+1)
            
            lval = query(left, mid, 2*indx)
            rval = query(mid+1, right, 2*indx+1)
            
            return lval + rval
        
        return query(left, right, 1)