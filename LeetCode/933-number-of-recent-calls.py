class RecentCounter:

    def __init__(self):
        self.queue = []        

    def ping(self, t: int) -> int:
        self.queue.insert(0, t)
        while self.queue[-1] < t-3000:
            self.queue.pop()
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)