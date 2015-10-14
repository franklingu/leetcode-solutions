/**
 * Given a sorted linked list, delete all nodes that have duplicate numbers,
 * leaving only distinct numbers from the original list.
 *
 * For example,
 * Given 1->2->3->3->4->4->5, return 1->2->5.
 * Given 1->1->1->2->3, return 2->3.
 *
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
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == NULL) {
            return head;
        }

        ListNode* pp = head;
        ListNode* p = head;
        ListNode* n = head -> next;
        bool dupFlag = false;

        while (n != NULL) {
            if (n -> val == p -> val) {
                dupFlag = true;
                p->next = n->next;
                delete n;
                n = p-> next;
            } else {
                if (dupFlag) {
                    p -> val = n -> val;
                    p -> next = n -> next;
                    delete n;
                    n = p -> next;
                    dupFlag = false;
                } else {
                    if (p != pp) {
                        pp = pp -> next;
                    }
                    p = p -> next;
                    n = n -> next;
                }
            }
        }

        if (dupFlag) {
            if (p != head) {
                pp -> next = NULL;
                delete p;
            } else {
                delete head;
                head = NULL;
            }
            dupFlag = false;
        }

        return head;
    }
};
