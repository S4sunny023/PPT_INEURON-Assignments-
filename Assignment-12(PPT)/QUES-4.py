class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    if head is None or head.next is None:
        return True

    slowPtr = head
    fastPtr = head

    # Traverse to find the middle node
    while fastPtr is not None and fastPtr.next is not None:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next

    # Reverse the second half of the linked list
    secondHalfHead = reverseLinkedList(slowPtr)

    # Compare the first and second halves of the linked list
    firstHalfPtr = head
    secondHalfPtr = secondHalfHead

    while secondHalfPtr is not None:
        if firstHalfPtr.val != secondHalfPtr.val:
            return False
        firstHalfPtr = firstHalfPtr.next
        secondHalfPtr = secondHalfPtr.next

    return True

def reverseLinkedList(head):
    prev = None
    curr = head

    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev

# Example usage
# Example 1
head1 = ListNode('R')
head1.next = ListNode('A')
head1.next.next = ListNode('D')
head1.next.next.next = ListNode('A')
head1.next.next.next.next = ListNode('R')

print("Linked list is a palindrome:", isPalindrome(head1))

# Example 2
head2 = ListNode('C')
head2.next = ListNode('O')
head2.next.next = ListNode('D')
head2.next.next.next = ListNode('E')

print("Linked list is a palindrome:", isPalindrome(head2))

