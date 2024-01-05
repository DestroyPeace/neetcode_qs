# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        dp = {}

        def dfs(val, curr): 
            if val == targetSum:
                return True 
            
            # Reached the end of this path.
            if not curr.left and not curr.right: 
                return False 
            
            if curr in dp:
                return dp[curr]
            
            dp[curr.left] = dfs(val + curr.left.val, curr.left)
            dp[curr.right] = dfs(val + curr.right.val, curr.right)

        dfs(0, root)
        return dp[root]


