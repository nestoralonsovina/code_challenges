def deleteNode(head, position):
    if position == 0:
        return head.next
    head.next = deleteNode(head.next, position - 1)
    return head
