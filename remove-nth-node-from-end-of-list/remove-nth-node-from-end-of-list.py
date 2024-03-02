# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
#         count = 1
#         curr = head
#         lst_head = head
        
#         if curr.next == None and n == 1:
#             return None
        
#         while curr.next != None:
#             curr = curr.next
#             count+= 1
        
#         curr = head
#         idx = count - n
        
#         if n == count:
#             head = head.next
#         print(head.val)
       
#         for i in range(idx-1):
#             curr = curr.next
#         curr.next = curr.next.next
#         return head

#two pointers

        fast = head
        slow = head

        for i in range(n):
            fast = fast.next

        # This situation would happen when we are required to del the first node (n = len(List))
            # Also, it can handle the [] case
        if not fast:
            return slow.next


        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head
            