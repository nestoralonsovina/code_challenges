def reverse(head):
    if not head or not head.next:
        return head
    newHead = reverse(head.next)
    head.next.next = head
    head.next = None
    return newHead
