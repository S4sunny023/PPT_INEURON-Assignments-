class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeDuplicates(head):
    if head is None or head.next is None:
        return head

    current = head
    while current is not None and current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head



# Example
# LinkedList: 11->11->11->21->43->43->60
head = Node(11)
head.next = Node(11)
head.next.next = Node(11)
head.next.next.next = Node(21)
head.next.next.next.next = Node(43)
head.next.next.next.next.next = Node(43)
head.next.next.next.next.next.next = Node(60)

head = removeDuplicates(head)

# Print the modified linked list
while head is not None:
    print(head.data, end=' ')
    head = head.next

