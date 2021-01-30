/**
 * Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
 *
 * Example:
 *
 * Input: The root of a Binary Search Tree like this:
 *               5
 *             /   \
 *            2     13
 *
 * Output: The root of a Greater Tree like this:
 *              18
 *             /   \
 *           20     13
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
class Solution {
    public TreeNode convertBST(TreeNode root) {
        return convertBSTWithRoot(root, root);
    }

    TreeNode convertBSTWithRoot(TreeNode curr, TreeNode root) {
        if (curr == null) {
            return curr;
        }
        TreeNode ret = new TreeNode(curr.val + sumLargerThan(root, curr.val));
        TreeNode left = convertBSTWithRoot(curr.left, root);
        TreeNode right = convertBSTWithRoot(curr.right, root);
        ret.left = left;
        ret.right = right;
        return ret;
    }

    int sumLargerThan(TreeNode root, int val) {
        if (root == null) {
            return 0;
        }
        int sumRight = sumLargerThan(root.right, val);
        if (root.val <= val) {
            return sumRight;
        }
        return sumRight + root.val + sumLargerThan(root.left, val);
    }
}
