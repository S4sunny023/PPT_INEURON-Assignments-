class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return None 

    def isEmpty(self):
        return len(self.queue) == 0
    


queue = Queue()
print(queue.isEmpty())  

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue()) 
print(queue.dequeue())  

print(queue.isEmpty())  
print(queue.dequeue())
print(queue.isEmpty())  


