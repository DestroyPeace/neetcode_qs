# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root) -> int:
        """global res
        res = 0

        def dfs(root, max_num):
            global res

            if not root:
                return 0

            if max_num > root.val:
                max_num = root.val
            else:
                res += 1
            
            dfs(root.right, max_num)
            dfs(root.left, max_num)
        
        dfs(root, root.val)

        return res"""
  

        def dfs(node, max_val):
            
            if not node:
                return 0 # Returning 0 because the tree is empty meaning that nothing is there
            
            res = 1 if node.val <= max_val else 0
            max_val = max(node.val, max_val)

            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)

            return res
        
        return dfs(root, root.val)



