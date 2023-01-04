def addTwoNumbers(l1, l2):
    l1_val = ""
    l2_val = ""

    # Getting all the value from linked list l1 
    while l1 is not None:
        l1_val += str(l1.val)
        l1 = l1.next

    # Getting all the value fro, linked list l2
    while l2 is not None:
        l2_val += str(l2.val)
        l2 =  l2.next

    # sum of the values from linked list l1 and l2
    lnked_list_sum = int(l1_val[::-1]) + int(l2_val[::-1])
    print(lnked_list_sum)

    # stores main head
    head = None

    # stores prev head for loop to assign its next
    prev_node = None

    for elem in str(lnked_list_sum)[::-1]: #708
        # creating a linked list
        node = ListNode()
        # assigning elem as linked list value
        node.val = elem
        # if prev_node exist, it's value remians true from second 
        if prev_node:
            prev_node.next = node
        else:
            # It is true only at first to set head
            head = node
        # updating prev node to current node before loop ends
        prev_node = node
    # next for last node
    prev_node.next = None
    return head
        