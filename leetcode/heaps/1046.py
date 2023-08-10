import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        # Converting each of the stones to negative numbers
        stones = [-s for s in stones] 

        # This allows the min heap that is created to be treated as a max heap

        heapq.heapify(stones)

        while len(stones) > 1:
            # Getting the two largest values.

            first = heapq.heappop(stones)
            second = heapq.heappop(stones) 

            # Checking the conditions of first == second and first > second 

            # The conditions are reversed due to the negative numbers involved.
            if second > first:
                heapq.heappush(stones, first - second)

            # The second condition can be ignored due to both stones being destroyed.

        return abs(stones[0]) if stones else 0
