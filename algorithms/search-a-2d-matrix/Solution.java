/**
 * Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has
 * the following properties:
 * 
 * Integers in each row are sorted from left to right.
 * The first integer of each row is greater than the last integer of the previous row.
 * For example,
 *   Consider the following matrix:
 *     [
 *      [1,   3,  5,  7],
 *      [10, 11, 16, 20],
 *      [23, 30, 34, 50]
 *     ]
 *   Given target = 3, return true.
 */

public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length <= 0 || matrix[0].length <= 0) {
            return false;
        }
        int N = matrix.length;
        int M = matrix[0].length;
        int start = 0, end = N - 1, mid = 0;
        int idx = 0;
        while (start < end) {
            mid = (start + end + 1) / 2;
            if (matrix[mid][0] > target) {
                end = mid - 1;
            } else if (matrix[mid][0] == target) {
                return true;
            } else {
                start = mid;
            }
        }
        idx = start;
        start = 0;
        end = M - 1;
        while (start < end) {
            mid = (start + end + 1) / 2;
            if (matrix[idx][mid] > target) {
                end = mid - 1;
            } else if (matrix[idx][mid] == target) {
                return true;
            } else {
                start = mid;
            }
        }
        return (matrix[idx][start] == target);
    }
}
