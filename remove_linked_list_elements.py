# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def removeElements(self, head, val):
        dummy_head = ListNode(next=head)
        prev, current = dummy_head, head

        while current:
            temp = current.next
            if current.val == val:
                prev.next = temp
            else:
                prev = current
            current = current.next
        return dummy_head.next


        