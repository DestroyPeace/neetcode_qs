"""
Initially thought Dijkstra's, however it is the Belmman Ford algo

Dijkstra is unable to be used due to the condition "at most k stops".
It's still doable in this, however another algo called the Belmman Ford algo is used.

Time Complexity: O(E . K)
and is typically a BFS 

It typically runs in O(E.V) where V is the number of vertices and E is the edges
Bellman Ford can deal with negative weights. 

The main idea is to start at the source node, and then use BFS to the K + 1 layers. 

"""

List = list 

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n 
        prices[src] = 0

        for i in range(k + 1):
            temp_prices = prices.copy()
            
            # Directed edges betwene the source and the destination.
            for s, d, p in flights: 
                # Unable to be reached.
                if prices[s] == float("inf"):
                    continue 
                
                temp_prices[d] = min(prices[s] + p, temp_prices[d])
        
            prices = temp_prices 

        return prices[dst] if prices[dst] != float("inf") else -1
    
test = Solution()
print(test.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0))

