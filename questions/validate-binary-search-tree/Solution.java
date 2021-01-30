/**
 * Given a binary tree, determine if it is a valid binary search tree (BST).
 *
 * Assume a BST is defined as follows:
 *
 * The left subtree of a node contains only nodes with keys less than the node's key.
 * The right subtree of a node contains only nodes with keys greater than the node's key.
 * Both the left and right subtrees must also be binary search trees.
 * Example 1:
 *
 * Input:
 *     2
 *    / \
 *   1   3
 * Output: true
 * Example 2:
 *
 *     5
 *    / \
 *   1   4
 *      / \
 *     3   6
 * Output: false
 * Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
 *              is 5 but its right child's value is 4.
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
    public boolean isValidBST(TreeNode root) {
        Integer[] res = isValidSubtree(root);
        return (res[0] == 1);
    }

    Integer[] isValidSubtree(TreeNode root) {
        if (root == null) {
            return new Integer[]{1, null, null};
        }
        Integer[] leftResult = isValidSubtree(root.left);
        Integer[] rightResult = isValidSubtree(root.right);
        if (leftResult[0] != 1 || rightResult[0] != 1) {
            return new Integer[]{0, null, null};
        }
        if (!(leftResult[2] == null || leftResult[2] < root.val) || !(rightResult[1] == null || rightResult[1] > root.val)) {
            return new Integer[]{0, null, null};
        }
        if (leftResult[1] == null) {
            leftResult[1] = root.val;
        }
        if (rightResult[2] == null) {
            rightResult[2] = root.val;
        }
        return new Integer[]{1, leftResult[1], rightResult[2]};
    }
}
