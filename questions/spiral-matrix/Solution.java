/**
 * Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
 * 
 * For example,
 * Given the following matrix:
 * 
 * [
 *  [ 1, 2, 3 ],
 *  [ 4, 5, 6 ],
 *  [ 7, 8, 9 ]
 * ]
 * You should return [1,2,3,6,9,8,7,4,5].
 */

public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        if (matrix == null || matrix.length <= 0) {
            return new ArrayList<Integer>();
        }
        List<Integer> results = new ArrayList<Integer>();
        int left = 0, right = matrix[0].length - 1, up = 0, down = matrix.length - 1, dir = 1;
        int row = 0, col = 0;
        
        while (col >= left && col <= right && row >= up && row <= down) {
            results.add(matrix[row][col]);
            if (left == right && up == down) {
                break;
            }
            if (dir == 1) {  // right
                if (col == right) {
                    dir = 2;
                    up++;
                    row++;
                } else {
                    col++;
                }
            } else if (dir == 2) {  // down
                if (row == down) {
                    dir = 3;
                    right--;
                    col--;
                } else {
                    row++;
                }
                
            } else if (dir == 3) {  // left
                if (col == left) {
                    dir = 4;
                    down--;
                    row--;
                } else {
                    col--;
                }
            } else if (dir == 4) {  // up
                if (row == up) {
                    dir = 1;
                    left++;
                    col++;
                } else {
                    row--;
                }
            }
        }
        
        return results;
    }
}
