/**
 * You are given a binary tree in which each node contains an integer value.
 *
 * Find the number of paths that sum to a given value.
 *
 * The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
 *
 * The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
 *
 * Example:
 *
 * root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
 *
 *       10
 *      /  \
 *     5   -3
 *    / \    \
 *   3   2   11
 *  / \   \
 * 3  -2   1
 *
 * Return 3. The paths that sum to 8 are:
 *
 * 1.  5 -> 3
 * 2.  5 -> 2 -> 1
 * 3. -3 -> 11
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
    public int pathSum(TreeNode root, int sum) {
        return pathSumCheck(root, sum, false);
    }

    int pathSumCheck(TreeNode root, int sum, boolean includeOnly) {
        if (root == null) {
            return 0;
        }
        int self = (root.val == sum) ? 1 : 0;
        int left2 = pathSumCheck(root.left, sum - root.val, true);
        int right2 = pathSumCheck(root.right, sum - root.val, true);
        if (includeOnly) {
            return self + left2 + right2;
        }
        int left1 = pathSumCheck(root.left, sum, false);
        int right1 = pathSumCheck(root.right, sum, false);
        return self + left2 + right2 + left1 + right1;
    }
}
