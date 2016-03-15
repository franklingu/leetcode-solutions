/**
 * Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
 *
 * For example:
 * Given the below binary tree and sum = 22,
 *               5
 *              / \
 *             4   8
 *            /   / \
 *           11  13  4
 *          /  \    / \
 *         7    2  5   1
 * return
 * [
 *    [5,4,11,2],
 *    [5,8,4,5]
 * ]
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
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        checkPathSum(root, sum, results);

        return results;
    }

    private int[] checkPathSum(TreeNode root, int sum, List<List<Integer>> mem) {
        int[] tmp = {0, -1};
        if (root == null) {
            return tmp;
        }
        if (root.left == null && root.right == null) {
            if (root.val == sum) {
                tmp[0] = 1;
                tmp[1] = mem.size();
                List<Integer> curr = new ArrayList<Integer>();
                curr.add(root.val);
                mem.add(curr);
            }
            return tmp;
        } else if (root.left == null) {
            int[] right = checkPathSum(root.right, sum - root.val, mem);
            if (right[0] == 1) {
                for (int i = 1; i < right.length; i++) {
                    mem.get(right[i]).add(0, root.val);
                }
            }
            return right;
        } else if (root.right == null) {
            int[] left = checkPathSum(root.left, sum - root.val, mem);
            if (left[0] == 1) {
                for (int i = 1; i < left.length; i++) {
                    mem.get(left[i]).add(0, root.val);
                }
            }
            return left;
        } else {
            int[] result;
            int[] left = checkPathSum(root.left, sum - root.val, mem);
            int[] right = checkPathSum(root.right, sum - root.val, mem);
            if (left[0] == 1) {
                for (int i = 1; i < left.length; i++) {
                    mem.get(left[i]).add(0, root.val);
                }
            }
            if (right[0] == 1) {
                for (int i = 1; i < right.length; i++) {
                    mem.get(right[i]).add(0, root.val);
                }
            }
            if (left[0] == 1 && right[0] == 1) {
                result = new int[left.length + right.length - 1];
                result[0] = 1;
                int runner = 1;
                for (int i = 1; i < left.length; i++) {
                    result[runner] = left[i];
                    runner++;
                }
                for (int i = 1; i < right.length; i++) {
                    result[runner] = right[i];
                    runner++;
                }
            } else if (left[0] == 1) {
                result = left;
            } else if (right[0] == 1) {
                result = right;
            } else {
                result = tmp;
            }
            return result;
        }
    }
}
