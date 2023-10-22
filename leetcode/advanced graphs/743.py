"""
Djikstra's Algo

Directed edges 

Times[i] is a triple value of (initial node, target node, distance / weight) 
Djikstra's algo is a breadth first search algorithm. It uses a min heap and is a shortest 
path algo

Starting node 

"""

import heapq 
import collections 

List = list 


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        # Getting all of the connections. 
        for u, v, w in times: 
            edges[u].append((v, w))

        # Frontier where the minimum path is used.
        min_heap = [(0, k)]
        visit = set()

        t = 0 

        
        while min_heap:
            # Taking the shortest next path.
            w1, n1 = heapq.heappop(min_heap)
            
            # If the node has already been visited - skip. 
            if n1 in visit:
                continue 

            visit.add(n1)
            t = w1

            # Checking any other edges by checking the neighbours:
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    # Total path to reach N2.
                    heapq.heappush(min_heap, (w1 + w2, n2))

        return t if len(visit) == n else - 1
    
