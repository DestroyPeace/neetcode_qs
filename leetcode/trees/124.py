# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # O(n) by checking each of the subtrees.

        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            # Calculating the max values of each of the children.
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # Ensuring that the values are not negative else we ignore them.
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]



