from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)


recentCounter = RecentCounter()
print(recentCounter.ping(1))    
print(recentCounter.ping(100)) 
print(recentCounter.ping(3001)) 
print(recentCounter.ping(3002))  



