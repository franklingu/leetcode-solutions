/**
 * Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
 *
 * The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
 * http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png
 * A partially filled sudoku which is valid.
 */

public class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[] mapping = new boolean[9];
        for (int i = 0; i < 9; i++) {
            resetMapping(mapping);
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    if (mapping[(int)(board[i][j]) - (int)('1')]) {
                        return false;
                    } else {
                        mapping[(int)(board[i][j]) - (int)('1')] = true;
                    }
                }
            }
        }
        for (int i = 0; i < 9; i++) {
            resetMapping(mapping);
            for (int j = 0; j < 9; j++) {
                if (board[j][i] != '.') {
                    if (mapping[(int)(board[j][i]) - (int)('1')]) {
                        return false;
                    } else {
                        mapping[(int)(board[j][i]) - (int)('1')] = true;
                    }
                }
            }
        }
        for (int i = 0; i < 9; i = i + 3) {
            for (int j = 0; j < 9; j = j + 3) {
                resetMapping(mapping);
                for (int k = 0; k < 3; k++) {
                    for (int m = 0; m < 3; m++) {
                        if (board[i + k][j + m] != '.') {
                            if (mapping[(int)(board[i + k][j + m]) - (int)('1')]) {
                                return false;
                            } else {
                                mapping[(int)(board[i + k][j + m]) - (int)('1')] = true;
                            }
                        }
                    }
                }
            }
        }

        return true;
    }

    private void resetMapping(boolean[] mapping) {
        for (int i = 0; i < mapping.length; i++) {
            mapping[i] = false;
        }
    }
}
