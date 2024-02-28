# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        
        slow = head
        
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
    
    
    
    # slow = fast = head
    # while fast and fast.next:
    #     slow = slow.next
    #     fast = fast.next.next
    #     if slow == fast:
    #         break
    # else:
    #     return None
    # while head != slow:
    #     slow = slow.next
    #     head = head.next
    # return head
            
                