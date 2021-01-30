/**
 * Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
 *
 * For example:
 * Given binary tree {3,9,20,#,#,15,7},
 *     3
 *    / \
 *   9  20
 *     /  \
 *    15   7
 * return its bottom-up level order traversal as:
 * [
 *   [15,7],
 *   [9,20],
 *   [3]
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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        List<List<Integer>> reversed = new ArrayList<List<Integer>>();
        traverseAndPutLevelOrder(root, 0, results);
        for (int i = results.size() - 1; i >= 0; i--) {
            reversed.add(results.get(i));
        }

        return reversed;
    }

    private void traverseAndPutLevelOrder(TreeNode node, int curr, List<List<Integer>> levels) {
        if (node == null) {
            return ;
        }
        List<Integer> tmp;
        if (curr >= levels.size()) {
            tmp = new ArrayList<Integer>();
            levels.add(tmp);
        } else {
            tmp = levels.get(curr);
        }
        tmp.add(node.val);
        traverseAndPutLevelOrder(node.left, curr + 1, levels);
        traverseAndPutLevelOrder(node.right, curr + 1, levels);
    }
}
