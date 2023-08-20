import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []

        heapq.heapify(self.min_heap)
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, num)
        
        

    def findMedian(self) -> float:
        length = len(self.min_heap)

        # Even case
        if length % 2 == 0:
            return (self.min_heap[length // 2 - 1] + self.min_heap[length // 2]) / 2
        else:
            return self.min_heap[(length + 1) // 2 - 1]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()