
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # Working backwards in order to find the heights. This allows me to store the 
        # heights rather than recalculating and revisiting nodes. This changes the 
        # time complexity from O(n^2) to something around O(n)

        def dfs(root):
            # If a root is null, it's balanced.
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)

            # Checking that the distance between the left and right subtrees is less than 1
            # and that the left and right subtrees themselves are balanced. 
            balanced = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1 

            # Calculating the height by taking the max of the children nodes because
            # this means that you are guaranteed the height due to finding the highest
            # node distance and adding 1 for the current node.
            height = 1 + max(left[1], right[1])

            # Returning the values that can be used for the function calls later on.
            return [balanced, height]
        
        return dfs(root)[0]

