# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root:TreeNode) -> bool:
        def isValid(node, lb, ub):
            # Empty BST is still a BST,
            if not node:
                return True

            # If a value that satisfies both of these, that means that it's invalid
            # Could also be written as 

            """
            if node.val > ub or node.val < lb:
            """

            if not(node.val < ub and node.val > lb):
                return False

            # Using two function calls to check both the left side and the right side
            # Interesting property is the fact that the left side has to be less than
            # the parent root. This means that the two function calls will use different
            # "inequalities"

            # For left, we set the highest boundary to the parent. This works because
            # if the parent isn't able to satify the previous inequality, e.g being
            # greater than a previous value, that means this won't be called. 

            # For the right, we want to set the lowest boundary to the parent to ensure
            # that the child is a greater value than the child. 

            # Returning the two values, whereby if they ever return true by reaching their children
            # it'll return true as both sides of the tree have reached their children without raising
            # the false case.
            return (isValid(node.left, lb, node.val) and 
            isValid(node.right, node.val, ub))

        # Calling the function using the two boundary points of infinity and -inf.

        return isValid(root, float("-inf"), float("inf"))



        

        
