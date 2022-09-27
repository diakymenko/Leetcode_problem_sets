# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dict_a = {}
        current_a = headA
        current_b = headB
        node = None

        while current_a:
            dict_a[current_a] = current_a.next
            current_a = current_a.next

        while current_b:
            if current_b in dict_a:
                node = current_b
                while current_b in dict_a:
                    if current_b.next != dict_a[current_b]:
                        return None
                    else:
                        current_b = current_b.next
            else:
                current_b = current_b.next
        return node
        