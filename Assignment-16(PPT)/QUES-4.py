from queue import Queue

def checkIncreasingOrder(queue):
    stack = []
    secondQueue = Queue()
    expected = 1

    while not queue.empty():
        front = queue.queue[0]
        queue.get()

        if front == expected:
            secondQueue.put(front)
            expected += 1
        else:
            if not stack or stack[-1] > front:
                stack.append(front)
            else:
                return "No"

    while stack:
        if stack.pop() == expected:
            secondQueue.put(expected)
            expected += 1
        else:
            return "No"

    return "Yes"

# Example usage:
queue = Queue()
queue.put(5)
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)

print(checkIncreasingOrder(queue))  


queue = Queue()
queue.put(5)
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)

print(checkIncreasingOrder(queue)) 

