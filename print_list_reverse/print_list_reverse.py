def reversePrint(head):
    if head.next:
        reversePrint(head.next)
    print(head.data)

