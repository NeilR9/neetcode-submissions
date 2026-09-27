#include <unordered_map>
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(head == nullptr) {
            return nullptr;
        }
        std::unordered_map<Node*, int> oldList;
        std::unordered_map<int, Node*> newList;
        Node* newHead = new Node(head->val);
        Node* curHead = head;
        Node* revHead = newHead;
        int index = 0;
        while (curHead != nullptr) {
            if(curHead->next != nullptr) {
                revHead->next = new Node(curHead->next->val);
            }
            oldList[curHead] = index;
            newList[index] = revHead;
            curHead = curHead->next;
            revHead = revHead->next;
            index += 1;
        }
        Node* oldPtr = head;
        Node* newPtr = newHead;

        while (oldPtr != nullptr) {
            if (oldPtr->random == nullptr) {
                newPtr->random = nullptr;
            }
            else {
                int curIndex = oldList[oldPtr->random];
                newPtr->random = newList[curIndex];
            }
            oldPtr = oldPtr->next;
            newPtr = newPtr->next;
        }
        return newHead;
    }
    
};
