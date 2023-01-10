# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        int_val = 0
        while head:
            int_val = 2*int_val+head.val
            head = head.next
        return int_val