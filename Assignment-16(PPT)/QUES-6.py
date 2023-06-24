def reverseKElements(queue, k):
    stack = []

    # Push the first k elements from the queue into the stack
    for _ in range(k):
        stack.append(queue.dequeue())

    # Dequeue the first k elements from the queue

    # Pop each element from the stack and enqueue it back into the queue
    while stack:
        queue.enqueue(stack.pop())

    # Enqueue the remaining elements from the queue back into the queue in their original order
    for _ in range(queue.size() - k):
        queue.enqueue(queue.dequeue())

# Example usage:
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

k = 3

reverseKElements(queue, k)

# Output: 3 2 1 4 5
while not queue.is_empty():
    print(queue.front(), end=" ")
    queue.dequeue()
