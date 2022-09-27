# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        set_a = set()
        current_a = headA
        current_b = headB
        node = None

        while current_a:
            set_a.add(current_a)
            current_a = current_a.next

        while current_b:
            if current_b in set_a:
                node = current_b
                break
            else:
                current_b = current_b.next
            
        return node
        