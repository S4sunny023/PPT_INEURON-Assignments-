class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeSortedLists(a, b):
    # Create a dummy node as the head of the merged list
    dummy = Node(0)
    currMerged = dummy

    # Initialize pointers to the heads of the input linked lists
    currA = a
    currB = b

    # Merge the lists
    while currA is not None and currB is not None:
        if currA.data <= currB.data:
            currMerged.next = currA
            currA = currA.next
        else:
            currMerged.next = currB
            currB = currB.next
        currMerged = currMerged.next

    # Attach the remaining nodes of the non-empty list
    if currA is not None:
        currMerged.next = currA
    elif currB is not None:
        currMerged.next = currB

    return dummy.next



# Example 1
# a: 5->10->15
# b: 2->3->20
a = Node(5)
a.next = Node(10)
a.next.next = Node(15)

b = Node(2)
b.next = Node(3)
b.next.next = Node(20)

merged = mergeSortedLists(a, b)

# Print the merged list
while merged is not None:
    print(merged.data, end=' ')
    merged = merged.next
# Output: 2 3 5 10 15 20

# Example 2
# a: 1->1
# b: 2->4
a = Node(1)
a.next = Node(1)

b = Node(2)
b.next = Node(4)

merged = mergeSortedLists(a, b)

# Print the merged list
while merged is not None:
    print(merged.data, end=' ')
    merged = merged.next
# Output: 1 1 2 4
