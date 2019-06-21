def removeDuplicates(head):
    if not head or not head.next:
        return head

    tmp = removeDuplicates(head.next)

    if head.next:
        if head.data == head.next.data:
            head.next = head.next.next

    return head
