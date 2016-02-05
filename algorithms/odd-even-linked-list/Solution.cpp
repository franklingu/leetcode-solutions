/**
 * Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
 *
 * You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
 * 
 * Example:
 * Given 1->2->3->4->5->NULL,
 * return 1->3->5->2->4->NULL.
 * 
 * Note:
 * The relative order inside both the even and odd groups should remain as it was in the input. 
 * The first node is considered odd, the second node even and so on ...
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
    ListNode* oddEvenList(ListNode* head) {
        if (head == NULL || head->next == NULL || head->next->next == NULL) {
            return head;
        }
        
        ListNode* evenHead = head->next;
        ListNode* curr = head->next->next;
        ListNode* prev = evenHead;
        ListNode* prevprev = head;
        
        bool isOddLength = false;
        
        while (curr != NULL) {
            prevprev->next = curr;
            prevprev = prev;
            prev = curr;
            curr = curr->next;
            
            isOddLength ^= true;
        }
        
        if(isOddLength) {
            prev->next = evenHead;
            prevprev->next = NULL;
        } else {
            prev->next = NULL;
            prevprev->next = evenHead;
        }
        
        return head;
    }
};

//Alternative Solution

/*
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return head;
        }
        
        ListNode* iter = head;
        ListNode* temp = NULL;
        ListNode* evenHead = head->next;
        
        bool isOddLength = true;
        
        for (; iter->next->next != NULL; iter=temp) {
            temp = iter->next;
            iter->next = iter->next->next;
            isOddLength ^= true;
        }
        
        if(isOddLength) {
            iter->next->next = NULL;
            iter->next = evenHead;
        } else {
            iter->next->next = evenHead;
            iter->next = NULL;
        }
        
        return head;
    }
};
*/