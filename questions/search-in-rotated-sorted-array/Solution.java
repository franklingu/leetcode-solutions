/**
 * Suppose a sorted array is rotated at some pivot unknown to you beforehand.
 * 
 * (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
 * 
 * You are given a target value to search. If found in the array return its index, otherwise return -1.
 * 
 * You may assume no duplicate exists in the array.
 */

public class Solution {
    public int search(int[] nums, int target) {
        if (nums == null && nums.length <= 0) {
            return -1;
        }
        int start = 0, end = nums.length - 1, mid = 0;
        while (start < end) {
            mid = (start + end + 1) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[start] <= nums[mid] && nums[mid] <= nums[end]) {
                if (nums[mid] < target) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            } else if (nums[start] >= nums[mid] && nums[mid] <= nums[end]) {
                if (nums[mid] < target) {
                    if (nums[end] < target) {
                        end = mid - 1;
                    } else if (nums[start] == target) {
                        return start;
                    } else {
                        start = mid + 1;
                    }
                } else {
                    end = mid - 1;
                }
            } else if (nums[start] <= nums[mid] && nums[mid] >= nums[end]) {
                if (nums[mid] < target) {
                    start = mid + 1;
                } else {
                    if (nums[start] > target) {
                        start = mid + 1;
                    } else if (nums[start] == target) {
                        return start;
                    } else {
                        end = mid - 1;
                    }
                }
            }
            System.out.format("%d %d\n", start, end);
        }
        return (nums.length > start && nums[start] == target) ? start : -1;
    }
}
