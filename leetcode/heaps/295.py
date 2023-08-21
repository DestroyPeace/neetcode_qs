import heapq

class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.large_heap = []

        # Creating two heaps to find the middle of the max_heap small_heap and the min_heap large_heap.
        heapq.heapify(self.small_heap)
        heapq.heapify(self.large_heap)
        

    def addNum(self, num: int) -> None:
        
        if self.large_heap and num > self.large_heap[0]:
            heapq.heappush(self.large_heap, num)
        else:
            heapq.heappush(self.small_heap, -1 * num)

        # Checking that the length of both lists is within 1 to ensure that it is possible to calculate
        # even / odd. 

        if len(self.small_heap) > len(self.large_heap) + 1:
            res = heapq.heappop(self.small_heap) * -1 # MAX_HEAP[0] -> MIN_HEAP[0]
            heapq.heappush(self.large_heap, res)

        if len(self.large_heap) > len(self.small_heap) + 1:
            res = heapq.heappop(self.large_heap) * -1
            heapq.heappush(self.small_heap, res)   

    def findMedian(self) -> float:

        if len(self.large_heap) > len(self.small_heap):
            return self.large_heap[0]
    
        elif len(self.small_heap) > len(self.large_heap):
            return self.small_heap[0] * -1

        return ((self.small_heap[0] * -1) + self.large_heap[0]) / 2
        

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()