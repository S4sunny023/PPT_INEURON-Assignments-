class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def deleteNode(head, position):
    if head is None:
        return None

    if position == 1:
        head = head.next
        if head is not None:
            head.prev = None
        return head

    curr = head
    count = 1

    while curr is not None and count < position:
        curr = curr.next
        count += 1

    if curr is None:
        return head

    curr.prev.next = curr.next
    if curr.next is not None:
        curr.next.prev = curr.prev

    return head


# Example 1
# LinkedList: 1 <--> 3 <--> 4
# x = 3
head = Node(1)
node1 = Node(3)
node2 = Node(4)

head.next = node1
node1.prev = head
node1.next = node2
node2.prev = node1

position = 3
head = deleteNode(head, position)

# Print the modified linked list
curr = head
while curr is not None:
    print(curr.data, end=' ')
    curr = curr.next


# Example 2
# LinkedList: 1 <--> 5 <--> 2 <--> 9
# x = 1
head = Node(1)
node1 = Node(5)
node2 = Node(2)
node3 = Node(9)

head.next = node1
node1.prev = head
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

position = 1
head = deleteNode(head, position)

# Print the modified linked list
curr = head
while curr is not None:
    print(curr.data, end=' ')
    curr = curr.next


