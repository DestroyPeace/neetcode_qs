List = list
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        res, i = {}, 0

        # Shallow copy sort - not in place
        for q in sorted(queries):
            # Finding all intervals.
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]

                # Length of interval and end point
                heapq.heappush(min_heap, (r - l + 1, r))

                i += 1
            
            # Removing all intervals that don't  belong.
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            res[q] = min_heap[0][0] if min_heap else -1

        return [res[q] for q in queries]
