# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next and head.next.next:
            slow, fast = head.next, head.next.next
        else:
            return False
        
        while fast:
            if slow.next:
                slow = slow.next
            else:
                return False
            
            if fast.next:
                if fast.next.next:
                    fast = fast.next.next
                else:
                    return False
            else:
                return False

            if slow == fast:
                return True

        return False
