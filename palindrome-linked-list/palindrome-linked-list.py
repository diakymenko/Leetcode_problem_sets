# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        mid = None
        curr = head
        count = 0
        
        while curr:
            count+= 1
            curr = curr.next
        if count % 2 != 0:
            mid = count // 2 + 1
        else:
             mid = count // 2
        
        mid_pointer = head
        
        for i in range(mid):
            mid_pointer = mid_pointer.next
        
        
        prev = None
        
        while mid_pointer:
            temp = mid_pointer.next
            mid_pointer.next = prev
            prev = mid_pointer
            mid_pointer = temp
        
        curr_a = head
        
        curr_b = prev
       
        
        while curr_b:
            if curr_a.val != curr_b.val:
                return False
            curr_a = curr_a.next
            curr_b = curr_b.next
        return True
       
    
             
        

            
        
        