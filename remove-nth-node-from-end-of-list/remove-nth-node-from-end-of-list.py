# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 1
        curr = head
        lst_head = head
        
        if curr.next == None and n == 1:
            return None
        
        while curr.next != None:
            curr = curr.next
            count+= 1
        print(count)
        
        curr = head
        idx = count - n
        print(idx)
        
        if n == count:
            head = head.next
        print(head.val)
     
       
        for i in range(idx-1):
            curr = curr.next
        curr.next = curr.next.next
        return head
            