/**
 * Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
 * https://leetcode.com/static/images/courses/range_sum_query_2d.png
 * Range Sum Query 2D
 * The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
 * 
 * Example:
 * Given matrix = [
 *   [3, 0, 1, 4, 2],
 *   [5, 6, 3, 2, 1],
 *   [1, 2, 0, 1, 5],
 *   [4, 1, 0, 1, 7],
 *   [1, 0, 3, 0, 5]
 * ]
 * 
 * sumRegion(2, 1, 4, 3) -> 8
 * sumRegion(1, 1, 2, 2) -> 11
 * sumRegion(1, 2, 2, 4) -> 12
 * Note:
 * You may assume that the matrix does not change.
 * There are many calls to sumRegion function.
 * You may assume that row1 ≤ row2 and col1 ≤ col2.
 */

public class NumMatrix {
    private int[][] sums;
    
    public NumMatrix(int[][] matrix) {
        if (matrix == null || matrix.length <= 0) {
            this.sums = null;
            return;
        }
        this.sums = new int[matrix.length][matrix[0].length];
        sums[0][0] = matrix[0][0];
        for (int i = 1; i < matrix.length; i++) {
            sums[i][0] = sums[i - 1][0] + matrix[i][0];
        }
        for (int j = 1; j < matrix[0].length; j++) {
            sums[0][j] = sums[0][j - 1] + matrix[0][j];
        }
        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[0].length; j++) {
                sums[i][j] = sums[i][j - 1] + sums[i - 1][j] - sums[i- 1][j - 1] + matrix[i][j];
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        if (this.sums == null) {
            return 0;
        }
        int result;
        result = sums[row2][col2];
        if (col1 > 0) {
            result = result - sums[row2][col1 - 1];
        }
        if (row1 > 0) {
            result = result - sums[row1 - 1][col2];
        }
        if (col1 > 0 && row1 > 0) {
            result = result + sums[row1 - 1][col1 - 1];
        }
        return result;
    }
}


// Your NumMatrix object will be instantiated and called as such:
// NumMatrix numMatrix = new NumMatrix(matrix);
// numMatrix.sumRegion(0, 1, 2, 3);
// numMatrix.sumRegion(1, 2, 3, 4);
