/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // create dummy ListNode and copy address to node pointer
        ListNode dummy(0);
        ListNode* node = &dummy;

        while (list1 != nullptr && list2 != nullptr) {
            // if TRUE, set next pointer of node to list1,
            // increment pointer of list1.
            // if FALSE, set next pointer of node to list2,
            // increment pointer of list2.
            if (list1->val <= list2->val) { 
                node->next = list1;
                list1 = list1->next;
            } else {
                node->next = list2;
                list2 = list2->next;
            }
            // increment pointer of node
            node = node->next;
        }

        // check if either list is empty
        // if so, set next pointer for node to non-empty list
        if (list1 != nullptr){
            node->next = list1;
        } else if (list2 != nullptr) {
            node->next = list2;
        } else {
            printf("WTF!!!\n");
        }
        return dummy.next;
    }
};
