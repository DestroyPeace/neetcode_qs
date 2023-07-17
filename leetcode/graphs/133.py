class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hash = {}

        def dfs(new_node):
            # Base case.
            if new_node in hash:
                return hash[new_node]
            
            copy = Node(new_node.val)
            hash[new_node] = copy 

            for neighbor in new_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy 

        return dfs(node) if node else None
        
                