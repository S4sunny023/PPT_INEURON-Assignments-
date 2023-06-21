class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertAtAlternate(first, second):
    if not second:
        return

    first_next = None
    second_next = None

    while first and second:
        first_next = first.next
        second_next = second.next

        first.next = second
        second.next = first_next

        first = first_next
        second = second_next

        if first_next:
            first_next = first_next.next

        if second_next:
            second_next = second_next.next

    if second:
        first.next = second

    second = None

    return first_head


# Example usage:

# Creating the first linked list: 5->7->17->13->11
first_head = Node(5)
first_head.next = Node(7)
first_head.next.next = Node(17)
first_head.next.next.next = Node(13)
first_head.next.next.next.next = Node(11)

# Creating the second linked list: 12->10->2->4->6
second_head = Node(12)
second_head.next = Node(10)
second_head.next.next = Node(2)
second_head.next.next.next = Node(4)
second_head.next.next.next.next = Node(6)

# Calling the insertAtAlternate function
first_head = insertAtAlternate(first_head, second_head)

# Printing the modified first list
# Output: 5->12->7->10->17->2->13->4->11->6
current = first_head
while current:
    print(current.data, end=" ")
    current = current.next

# Printing the modified second list
# Output: None
print(second_head)
