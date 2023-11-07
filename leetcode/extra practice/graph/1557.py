import collections 

List = list 

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # Plan is to simply check for nodes where there are no roots.
        incoming = collections.defaultdict(int)
        
        for src, dest in edges: 
            incoming[dest] = incoming[dest] + 1

        res = []
        
        for i in range(n):
            if incoming[i] == 0:
                res.append(i)

        return res 
    
test = Solution()
print(test.findSmallestSetOfVertices(n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]))