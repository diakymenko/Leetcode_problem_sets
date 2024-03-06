# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
#     def addNode(l3, curr3, l1):
#         while l1:
#             sum_val = l1.val + incr_number
#             incr_number = 0
#             if sum_val > 9:
#                 incr_number = sum_val // 10
#                 sum_val = sum_val % 10
#             curr3.next = ListNode(sum_val)
#             curr3 = curr3.next
#             l1 = l1.next
#         if incr_number != 0:
#             curr3.next = ListNode(incr_number)

#         return l3.next
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def addNode(l3, curr3, l1, incr_number):
            while l1:
                sum_val = l1.val + incr_number
                incr_number = 0
                if sum_val > 9:
                    incr_number = sum_val // 10
                    sum_val = sum_val % 10
                curr3.next = ListNode(sum_val)
                curr3 = curr3.next
                l1 = l1.next
            if incr_number != 0:
                curr3.next = ListNode(incr_number)

            return l3.next
        
        l3 = ListNode() 
        curr3 = l3
        incr_number = 0
        
        while l1 and l2:
            sum_val = l1.val + l2.val + incr_number
            incr_number = 0
            if sum_val > 9:
                incr_number = sum_val // 10
                sum_val = sum_val % 10
            curr3.next = ListNode(sum_val)
            curr3 = curr3.next
            l1 = l1.next
            l2 = l2.next
            
        
        if l1:
            return addNode(l3, curr3, l1, incr_number)
        if l2:
            return addNode(l3, curr3, l2, incr_number)
        if incr_number != 0:
            curr3.next = ListNode(incr_number)

        return l3.next
        
        
    

    
    
            

   
            
            
        
        