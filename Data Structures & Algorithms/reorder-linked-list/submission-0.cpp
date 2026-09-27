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
    ListNode* getLastNodePrev(ListNode* curNode) {
        if(curNode->next == nullptr) {
            return curNode;
        }
        while(curNode->next->next != nullptr) {
            curNode = curNode->next;
        }
        return curNode;
    }
    void reorderList(ListNode* head) {
        if(head->next == nullptr || head->next->next == nullptr) {
            return;
        }
        ListNode * left = head;
        ListNode * rightPrev = getLastNodePrev(left);
        while (left != rightPrev) {
            ListNode * right = rightPrev->next;
            rightPrev->next = nullptr;
            right->next = left->next;
            left->next = right;
            left = right->next;
            rightPrev = getLastNodePrev(left);
        }
    }
};
