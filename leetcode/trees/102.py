class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        from collections import deque

        q = deque([root])
        final_res = []

        while q:
            res = []
            for _ in range(len(q)):
                node = q.popleft()

                # The node will always be non - null because of the first base case
                # and the subsequent base checks (checking if there is a value)
                res.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            final_res.append(res)
        
        return final_res
