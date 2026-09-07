# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head 

        while curr: 
            #save the rest of the list 
            next_node = curr.next
            #reverse the link 
            curr.next = prev
            #move prev forward
            prev = curr
            #move curr forward
            curr = next_node
        return prev

