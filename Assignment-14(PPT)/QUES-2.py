class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addOne(head):
    if head is None:
        return None

    # Traverse the list to find the rightmost node with a value less than 9
    curr = head
    lastLessThanNine = None

    while curr is not None:
        if curr.data < 9:
            lastLessThanNine = curr
        curr = curr.next

    # If a node with value less than 9 is found, increment its value by 1
    if lastLessThanNine is not None:
        lastLessThanNine.data += 1
        curr = lastLessThanNine.next

    # Set all the nodes to the right of the current node (including the current node) to 0
    while curr is not None:
        curr.data = 0
        curr = curr.next

    # If all digits were 9, add a new node with value 1 at the beginning
    if lastLessThanNine is None:
        newHead = Node(1)
        newHead.next = head
        head = newHead

    return head



# Example 1
# LinkedList: 4 -> 5 -> 6
head = Node(4)
node1 = Node(5)
node2 = Node(6)

head.next = node1
node1.next = node2

head = addOne(head)

# Print the modified linked list
curr = head
while curr is not None:
    print(curr.data, end='')
    curr = curr.next

# Example 2
# LinkedList: 1 -> 2 -> 3
head = Node(1)
node1 = Node(2)
node2 = Node(3)

head.next = node1
node1.next = node2

head = addOne(head)

# Print the modified linked list
curr = head
while curr is not None:
    print(curr.data, end='')
    curr = curr.next

