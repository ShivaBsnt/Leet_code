# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):

        # checking if it is a single node with no connection
        if not head or not head.next:
            return None

        # setting slow and fast pointer
        # if head = [3, 2, 0, -4], slow_pointer=3 and fast_pointer= 0
        slow_pointer, fast_pointer = head, head
        is_cycle = False

        # since the fast pointer moves fast, checking fast_pointer and fast_pointer.next
        # if it is not cycle then fast_pointer.next is None
        while fast_pointer and fast_pointer.next:

            # moving pointers to next nodes
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            # checking if two pointer has met each other
            if slow_pointer == fast_pointer:
                is_cycle = True
                break


        if not is_cycle:
            return None

        if is_cycle:
            start=head
            while start != slow_pointer:
                start = start.next
                slow_pointer=slow_pointer.next
        return start
            


            
