def compareLists(l1, l2):
    if not l1 and not l2:
        return 1
    if (l1 and not l2) or (not l1 and l2):
        return 0
    if l1.data != l2.data:
        return 0
    if l1.data and l2.data:
        compareLists(l1.next, l2.next)
