class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def printList(head):
    curr = head
    while curr:
        random_data = curr.random.data if curr.random else None
        print(f"Data: {curr.data}, Random: {random_data}")
        curr = curr.next

def copyRandomList(head):
    if not head:
        return None

    # Step 1: Create a copy of each node and insert it between the original nodes
    curr = head
    while curr:
        new_node = Node(curr.data)
        new_node.next = curr.next
        curr.next = new_node
        curr = new_node.next

    # Step 2: Set the random pointers for the copied nodes
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate the original list and the copied list
    original = head
    copied = head.next
    copied_head = copied

    while original:
        original.next = original.next.next
        copied.next = copied.next.next if copied.next else None
        original = original.next
        copied = copied.next

    return copied_head

# Example 1
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

head.random = head.next
head.next.random = head.next.next.next

print("Original List:")
printList(head)
# Output:
# Data: 1, Random: 2
# Data: 2, Random: 4
# Data: 3, Random: None
# Data: 4, Random: None

copied_head = copyRandomList(head)

print("Copied List:")
printList(copied_head)


# Example 2
head = Node(1)
head.next = Node(3)
head.next.next = Node(5)
head.next.next.next = Node(9)

head.random = head
head.next.random = head.next.next.next

print("Original List:")
printList(head)


copied_head = copyRandomList(head)

print("Copied List:")
printList(copied_head)

