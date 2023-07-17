# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1
            
            left = dfs(root.left) # Finding the height of the left sub tree
            right = dfs(root.right) # Finding the height of the right sub tree

            res[0] = max(res[0], 2 + left + right) # Updating the max diameter

            return 1 + max(left, right) # Returning the height.
        
        dfs(root)
        return res[0]
