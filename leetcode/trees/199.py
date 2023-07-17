class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:    
    def rightSideView(self, root: TreeNode) -> list[int]:
        """if not root:
            return []
        
        res = [root.val]
        
        while root:
            if root.right:
                root = root.right
                res.append(root.val)
            elif root.left:
                root = root.left
                res.append(root.val)

            else:
                return res"""

        from collections import deque

        res = []

        if not root:
            return []

        q = deque([root])

        while q:
            right_side = None

            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)

            if right_side:
                res.append(right_side.val)
        
        return res
            





        