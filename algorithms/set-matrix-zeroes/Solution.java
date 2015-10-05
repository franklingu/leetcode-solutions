/**
 * Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
 */

public class Solution {
    public void setZeroes(int[][] matrix) {
        if (matrix.length <= 0 || matrix[0].length <= 0) {
            return ;
        }
        int N = matrix.length;
        int M = matrix[0].length;
        boolean[] rows = new boolean[M];
        boolean[] cols = new boolean[N];
        
        for (int i = 0; i < N; i++) {
            cols[i] = false;
        }
        for (int j = 0; j < M; j++) {
            rows[j] = false;
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (matrix[i][j] == 0) {
                    rows[j] = true;
                    cols[i] = true;
                }
            }
        }
        for (int i = 0; i < N; i++) {
            if (cols[i]) {
                for (int j = 0; j < M; j++) {
                    matrix[i][j] = 0;
                }
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (rows[j]) {
                    matrix[i][j] = 0;
                }
            }
        }
        return ;
    }
}
