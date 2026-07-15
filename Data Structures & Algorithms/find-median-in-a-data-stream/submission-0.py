class MedianFinder:

    def __init__(self):
        # max heap
        self.sHalf = []
        # min heap
        self.bHalf = []

    def addNum(self, num: int) -> None:
        if not self.sHalf:
            heapq.heappush(self.sHalf, -num)
            return
        
        if num > -self.sHalf[0]:
            heapq.heappush(self.bHalf, num)
        else:
            heapq.heappush(self.sHalf, -num)
        
        if len(self.sHalf) > len(self.bHalf) + 1:
            tmp = -heapq.heappop(self.sHalf)
            heapq.heappush(self.bHalf, tmp)
        elif len(self.sHalf) + 1 < len(self.bHalf):
            tmp = heapq.heappop(self.bHalf)
            heapq.heappush(self.sHalf, -tmp)

    def findMedian(self) -> float:
        if len(self.sHalf) == len(self.bHalf):
            return (-self.sHalf[0] + self.bHalf[0]) / 2
        elif len(self.sHalf) > len(self.bHalf):
            return -self.sHalf[0]
        else:
            return self.bHalf[0]
        