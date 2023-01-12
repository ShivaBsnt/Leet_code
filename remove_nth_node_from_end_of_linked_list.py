# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):

        # creating dummy node whose next is head
        dummy_node = ListNode(next=head)
        # left pointer
        left = dummy_node
        #right pointer
        right = head

        #shifting right pointer to n position
        while n>0 and right:
            right = right.next
            n -= 1

        # moving left and right pointer until and unless right is not None
        while right:
            left = left.next
            right = right.next
            
        # left.next is the node we wanted to delete so pointing left.next to left.next.next
        left.next = left.next.next

        # returning dummy_node.next whose next is head
        return dummy_node.next
