# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        prev = head 
        curr = head
        
        while(curr and curr.next):
            curr = curr.next.next
            prev= prev.next
            if(prev==curr):
                slow = prev
                while(head!=slow):
                    head = head.next
                    slow = slow.next
                return head
        return None
        