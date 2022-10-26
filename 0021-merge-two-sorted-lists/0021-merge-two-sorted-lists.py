# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        elif not list2:
            return list1
        
        current1 = list1
        current2 = list2
        
        
        w = dummy = ListNode()
        
        
        # if list1.val <= list2.val:
        #     head = list1
        #     current1 = head.next
        #     current2 = list2
        # else:
        #     head = list2
        #     current2 = head.next
        #     current1 = list1
        
            
        while current1 and current2:
            if current1.val <= current2.val:
                w.next = current1
                w = w.next
                current1 = current1.next
            else:
                w.next = current2
                w = w.next
                current2 = current2.next
                    
    
        w.next = current1 or current2
            
                
        return dummy.next
                