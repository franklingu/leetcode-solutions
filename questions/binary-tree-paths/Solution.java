/**
 * Given a binary tree, return all root-to-leaf paths.
 * 
 * For example, given the following binary tree:
 * 
 *    1
 *  /   \
 * 2     3
 *  \
 *   5
 * All root-to-leaf paths are:
 * 
 * ["1->2->5", "1->3"]
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
    public List<String> binaryTreePaths(TreeNode root) {
        List<StringBuilder> results = findPathsInBinaryTree(root);
        List<String> rs = new ArrayList<String>();
        if (results == null) {
            return rs;
        }
        for (StringBuilder sb : results) {
            rs.add(sb.toString());
        }
        return rs;
    }
    
    private List<StringBuilder> findPathsInBinaryTree(TreeNode root) {
        if (root == null ) {
            return null;
        }
        List<StringBuilder> lt = findPathsInBinaryTree(root.left);
        List<StringBuilder> rt = findPathsInBinaryTree(root.right);
        List<StringBuilder> results;
        if (lt == null && rt == null) {
            results = new ArrayList<StringBuilder>();
            results.add(new StringBuilder(Integer.toString(root.val)));
        } else if (lt == null) {
            results = rt;
            for (StringBuilder sb : results) {
                sb.insert(0, String.format("%d->", root.val));
            }
        } else if (rt == null) {
            results = lt;
            for (StringBuilder sb : results) {
                sb.insert(0, String.format("%d->", root.val));
            }
        } else {
            results = rt;
            for (StringBuilder sb : lt) {
                results.add(sb);
            }
            for (StringBuilder sb : results) {
                sb.insert(0, String.format("%d->", root.val));
            }
        }
        
        return results;
    }
}
