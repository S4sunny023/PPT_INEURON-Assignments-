class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextLargerNodes(head):
    stack = []
    answer = []
    index = 1
    
    while head:
        while stack and head.val > answer[stack[-1]]:
            answer[stack.pop()] = head.val
        
        stack.append(index)
        answer.append(0)
        
        head = head.next
        index += 1
    
    return answer


# Example 1
head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(5)

print(nextLargerNodes(head))  
# Example 2
head = ListNode(2)
head.next = ListNode(7)
head.next.next = ListNode(4)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)

print(nextLargerNodes(head)) 