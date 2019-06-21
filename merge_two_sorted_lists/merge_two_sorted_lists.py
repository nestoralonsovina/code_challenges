def mergeLists(head1, head2):
    if not head1 and not head2:
        return None

    if not head1:
        return head2

    if not head2:
        return head1

    if head1.data < head2.data:
        smaller_node = head1
        smaller_node.next = mergeLists(head1.next, head2)
    else:
        smaller_node = head2
        smaller_node.next = mergeLists(head1, head2.next)

    return smaller_node


