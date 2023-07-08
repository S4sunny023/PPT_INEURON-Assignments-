from collections import deque

class DataStream:
    def __init__(self, value, k):
        self.stream = deque()
        self.value = value
        self.k = k

    def consec(self, num):
        self.stream.append(num)

        if len(self.stream) < self.k:
            return False
        elif len(self.stream) > self.k:
            self.stream.popleft()

        return all(x == self.value for x in self.stream)



dataStream = DataStream(4, 3)
print(dataStream.consec(4)) 
print(dataStream.consec(4)) 
print(dataStream.consec(4))  
print(dataStream.consec(3)) 
