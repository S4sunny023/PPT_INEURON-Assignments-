class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None  

    def isEmpty(self):
        return len(self.stack) == 0


stack = Stack()
print(stack.isEmpty()) 

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  
print(stack.pop())  

print(stack.isEmpty())  
print(stack.pop()) 
print(stack.isEmpty()) 
