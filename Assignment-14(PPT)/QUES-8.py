class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    dummy = ListNode(0)
    dummy.next = head
    
    cumulative_sum = 0
    hashmap = {}
    current = dummy
    
    while current:
        cumulative_sum += current.val
        
        if cumulative_sum in hashmap:
            node = hashmap[cumulative_sum]
            node.next = current.next
            cumulative_sum += current.val
            
            while node.next != current:
                cumulative_sum += node.next.val
                del hashmap[cumulative_sum]
                node.next = node.next.next
        
        else:
            hashmap[cumulative_sum] = current
        
        current = current.next
    
    return dummy.next


# Example 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(-3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(1)

result = removeZeroSumSublists(head)
while result:
    print(result.val, end=' ')
    result = result.next


print()

# Example 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(-3)
head.next.next.next.next = ListNode(4)

result = removeZeroSumSublists(head)
while result:
    print(result.val, end=' ')
    result = result.next


print()

# Example 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(-3)
head.next.next.next.next = ListNode(-2)

result = removeZeroSumSublists(head)
while result:
    print(result.val, end=' ')
    result = result.next


