class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def skipAndDelete(head, M, N):
    count = 0
    current = head
    prev = None

    while current:
        count += 1

        if count < M:
            current = current.next
        elif count == M:
            temp = current.next

            for _ in range(N):
                if current.next:
                    current = current.next
                else:
                    break

            if prev:
                prev.next = current
            else:
                head = current

            count = 0
        else:
            break

        prev = current

    return head


# Example usage:

# Creating the linked list
# Input: 1->2->3->4->5->6->7->8
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

M = 2
N = 2

# Calling the skipAndDelete function
head = skipAndDelete(head, M, N)

# Printing the modified linked list
# Output: 1->2->5->6
current = head
while current:
    print(current.data, end=" ")
    current = current.next
