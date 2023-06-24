class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

def merge(a, b):
    # If one of the lists is empty, return the other list
    if a is None:
        return b
    if b is None:
        return a

    # Create a dummy node to hold the result
    dummy = Node(0)
    result = dummy

    # Merge the lists in sorted order
    while a is not None and b is not None:
        if a.data <= b.data:
            result.bottom = a
            a = a.bottom
        else:
            result.bottom = b
            b = b.bottom
        result = result.bottom

    # Append the remaining nodes of the non-empty list
    if a is not None:
        result.bottom = a
    else:
        result.bottom = b

    return dummy.bottom

def flatten(head):
    if head is None or head.next is None:
        return head

    # Recursively merge the sub-linked lists
    head.next = flatten(head.next)

    # Merge the current merged list with the next sub-linked list
    head = merge(head, head.next)

    return head

def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.bottom
    print()

# Example 1
head = Node(5)
head.next = Node(10)
head.next.next = Node(19)
head.next.next.next = Node(28)

head.bottom = Node(7)
head.bottom.bottom = Node(8)
head.bottom.bottom.bottom = Node(30)

head.next.bottom = Node(20)

head.next.next.bottom = Node(22)
head.next.next.next.bottom = Node(35)

head.next.bottom.bottom = Node(50)
head.next.next.bottom.bottom = Node(40)
head.next.next.bottom.bottom.bottom = Node(45)

head = flatten(head)

print("Flattened List:")
printList(head)


# Example 2
head = Node(5)
head.next = Node(10)
head.next.next = Node(19)
head.next.next.next = Node(28)

head.bottom = Node(7)
head.bottom.bottom = Node(22)
head.bottom.bottom.bottom = Node(30)

head.next.bottom = Node(50)

head = flatten(head)

print("Flattened List:")
printList(head)

