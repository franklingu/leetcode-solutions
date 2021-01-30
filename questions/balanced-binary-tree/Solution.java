/**
 * Given a binary tree, determine if it is height-balanced.
 *
 * For this problem, a height-balanced binary tree is defined as a binary
 * tree in which the depth of the two subtrees of every node never differ by more than 1.
 *
 */

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isBalanced(TreeNode root) {
        int[] results = checkBalanceAndDepth(root);

        return (results[0] == 1);
    }

    private int[] checkBalanceAndDepth(TreeNode root) {
        int[] results = {1, 0};
        if (root == null) {
            return results;
        }
        int depth = 0;
        int balanced = 0;
        int[] left = checkBalanceAndDepth(root.left);
        int[] right = checkBalanceAndDepth(root.right);
        if (left[0] == 0 || right[0] == 0) {
            results[0] = 0;
        } else {
            if (left[1] > right[1]) {
                results[0] = (left[1] - right[1] <= 1) ? 1 : 0;
            } else {
                results[0] = (right[1] - left[1] <= 1) ? 1 : 0;
            }
        }
        results[1] = ((left[1] > right[1]) ? left[1] : right[1]) + 1;
        return results;
    }
}
