class FrontMiddleBackQueue:
    def __init__(self):
        self.front_half = []
        self.back_half = []

    def pushFront(self, val):
        self.front_half.append(val)

    def pushMiddle(self, val):
        if len(self.front_half) > len(self.back_half):
            self.back_half.insert(0, self.front_half.pop())
        self.front_half.append(val)

    def pushBack(self, val):
        self.back_half.append(val)

    def popFront(self):
        if self.front_half:
            return self.front_half.pop()
        elif self.back_half:
            return self.back_half.pop(0)
        else:
            return -1

    def popMiddle(self):
        if len(self.front_half) == len(self.back_half):
            return self.front_half.pop()
        else:
            return self.back_half.pop(0) if self.back_half else -1

    def popBack(self):
        if self.back_half:
            return self.back_half.pop()
        elif self.front_half:
            return self.front_half.pop()
        else:
            return -1


q = FrontMiddleBackQueue()
print(q.pushFront(1))   
print(q.pushBack(2))     
print(q.pushMiddle(3))   
print(q.pushMiddle(4))   
print(q.popFront())      
print(q.popMiddle())    
print(q.popMiddle())     
print(q.popBack())       
print(q.popFront())    
