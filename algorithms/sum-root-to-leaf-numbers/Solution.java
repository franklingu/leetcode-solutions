/**
 * Given a binary tree containing digits from 0-9 only, each root-to-leaf path
 * could represent a number.
 *
 * An example is the root-to-leaf path 1->2->3 which represents the number 123.
 *
 * Find the total sum of all root-to-leaf numbers.
 *
 * For example,
 *
 *     1
 *    / \
 *   2   3
 * The root-to-leaf path 1->2 represents the number 12.
 * The root-to-leaf path 1->3 represents the number 13.
 *
 * Return the sum = 12 + 13 = 25.
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
    public int sumNumbers(TreeNode root) {
        List<StringBuilder> numSbs = toLeafNumbers(root);
        int result = 0;
        for (StringBuilder sb : numSbs) {
            result += Integer.parseInt(sb.toString());
        }

        return result;
    }

    private List<StringBuilder> toLeafNumbers(TreeNode root) {
        if (root == null) {
            return new ArrayList<StringBuilder>();
        }
        List<StringBuilder> leftNumbers = toLeafNumbers(root.left);
        List<StringBuilder> rightNumbers = toLeafNumbers(root.right);
        leftNumbers.addAll(rightNumbers);
        for (int i = 0; i < leftNumbers.size(); i++) {
            leftNumbers.get(i).insert(0, root.val);
        }
        if (leftNumbers.size() == 0) {
            StringBuilder sb = new StringBuilder();
            sb.append(root.val);
            leftNumbers.add(sb);
        }
        return leftNumbers;
    }
}
