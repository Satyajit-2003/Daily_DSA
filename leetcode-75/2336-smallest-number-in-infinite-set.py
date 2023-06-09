class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []       
        for i in range(1, 1001):
            heappush(self.heap, i)
            
    def popSmallest(self) -> int:
        return heappop(self.heap)

    def addBack(self, num: int) -> None:
        if num not in self.heap:
            heappush(self.heap, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)