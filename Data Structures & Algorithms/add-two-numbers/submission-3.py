# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return None
        
        dummy = ListNode()
        head = dummy
        carry = 0
        
        while l1 or l2:
            lsum = carry

            if l1:
                lsum += l1.val
                l1 = l1.next
            if l2:
                lsum += l2.val
                l2 = l2.next
            
            new_node = ListNode()

            carry = lsum // 10
            new_node.val = lsum % 10
            
            dummy.next = new_node
            dummy = dummy.next

        if carry:
            dummy.next = ListNode(1)

        return head.next
        