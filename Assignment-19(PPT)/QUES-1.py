import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
   
    heap = []
    
   
    for lst in lists:
        if lst:
            heapq.heappush(heap, (lst.val, lst))
    
   
    dummy = ListNode(0)
    curr = dummy
    
   
    while heap:
       
        _, node = heapq.heappop(heap)
        
       
        curr.next = node
        curr = curr.next
        
       
        if node.next:
            heapq.heappush(heap, (node.next.val, node.next))
    
    
    return dummy.next



lists1 = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]
merged1 = mergeKLists(lists1)
while merged1:
    print(merged1.val, end="->")
    merged1 = merged1.next

print()


lists2 = []
merged2 = mergeKLists(lists2)
while merged2:
    print(merged2.val, end="->")
    merged2 = merged2.next

print()


lists3 = [[]]
merged3 = mergeKLists(lists3)
while merged3:
    print(merged3.val, end="->")
    merged3 = merged3.next

print()