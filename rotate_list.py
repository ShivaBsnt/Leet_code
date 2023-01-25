# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotation(self, head):
        dummy_head = ListNode(next=head)
        prev = head
        curr = head.next

        while curr is not None:
            temp = curr.next
            if temp is None:
                prev.next = None
                curr.next = dummy_head.next
                dummy_head.next = curr
            prev = curr
            curr = temp
        return dummy_head.next

    def rotateRight(self, head, k):
        new_head = head
        if new_head is None or new_head.next is None:
            return new_head
        
        if k == 1:
            new_head = self.rotation(new_head)
            return new_head
        length, tail =1, head
        
        while tail.next: 
            tail = tail.next
            length+=1
            
        k = k%length
        for i in range(k):
            new_head = self.rotation(new_head)
        return new_head
