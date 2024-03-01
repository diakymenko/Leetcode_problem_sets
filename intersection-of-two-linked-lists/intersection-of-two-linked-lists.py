# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        set_a = set()
        
        curr = headA
        set_a = {curr}
       
        
        while curr.next != None:
            curr = curr.next
            set_a.add(curr)
        
        curr = headB
        
        if curr in set_a:
            return curr
        
        while curr.next != None:
            curr = curr.next
            if curr in set_a:
                return curr