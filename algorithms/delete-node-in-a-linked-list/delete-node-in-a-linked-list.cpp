/**
 * Write a function to delete a node (except the tail) 
 * in a singly linked list, given only access to that node.
 *
 * Supposed the linked list is 1 -> 2 -> 3 -> 4 and you 
 * are given the third node with value 3, the linked list 
 * should become 1 -> 2 -> 4 after calling your function.
 */


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * copy values over from the rest of the list
     * @node: pointer to the node to be deleted
     */
    void deleteNode(ListNode* node) {
        if (node == NULL) {
            return;
        }
        
        ListNode* prev = node;
        
        while (node -> next != NULL) {
            node -> val = node -> next -> val;
            prev = node;
            node = node -> next;
        }
        prev -> next = NULL;
        delete node;
    }
};