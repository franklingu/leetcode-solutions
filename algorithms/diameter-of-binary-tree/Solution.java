/**
 *  Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
 *
 * Example:
 * Given a binary tree
 *
 *           1
 *          / \
 *         2   3
 *        / \
 *       4   5
 *
 * Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
 *
 * Note: The length of path between two nodes is represented by the number of edges between them.
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
class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
        int[] res = findDiameter(root);
        return res[1];
    }

    int[] findDiameter(TreeNode root) {
        int[] res = new int[2];
        if (root == null) {
            return res;
        }
        int[] left = findDiameter(root.left);
        int[] right = findDiameter(root.right);
        int depth, dia;
        if (left[0] > right[0]) {
            depth = left[0] + 1;
        } else{
            depth = right[0] + 1;
        }
        dia = left[0] + right[0];
        if (dia < left[1]) {
            dia = left[1];
        }
        if (dia < right[1]) {
            dia = right[1];
        }
        res[0] = depth;
        res[1] = dia;
        return res;
    }
}
