class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if not head or not head.next:
        return head

    odd_head = head
    odd_tail = head
    even_head = head.next
    even_tail = head.next

    curr = head.next.next
    index = 3

    while curr:
        if index % 2 == 1:
            odd_tail.next = curr
            odd_tail = curr
        else:
            even_tail.next = curr
            even_tail = curr

        curr = curr.next
        index += 1

    even_tail.next = None
    odd_tail.next = even_head

    return odd_head
