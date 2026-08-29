# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slowPointer = head
        fastPointer = head
        prevPointer = None
        curIndex = 1
        while curIndex < n:
            fastPointer = fastPointer.next
            curIndex += 1
        while slowPointer != None and fastPointer.next != None:
            prevPointer = slowPointer
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
        if slowPointer == head:
            head = head.next
        elif slowPointer.next == None:
            prevPointer.next = None
        else:
            prevPointer.next = slowPointer.next
        return head
        


        