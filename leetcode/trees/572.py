# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def isSametree(root, subRoot) -> bool:
            if not root and not subRoot:
                return True
            
            if root and subRoot and (root.val == subRoot.val):
                return (isSametree(root.left, subRoot.left) and
                isSametree(root.right, subRoot.right))

        # Any null nodes are guaranteed to be part of a subroot by being at the end.
        if not subRoot:
            return True
        
        # Checking if the root is null, and the subRoot isn't null (previous check)
        if not root:
            return False

        if isSametree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        """if root.val != subRoot.val:
            self.isSubtree(root.left, subRoot)
            self.isSubtree(root.right, subRoot)
        
        else:
            if (root.left == subRoot.left) and (root.right == subRoot.right):
                return True"""

        # ITERATE THROUGH THE ROOT UNTIL SIMILAR VALUES ARE FOUND USING DFS.
"""        if root.val == subRoot.val:
            return (self.isSubtree(root.left, subRoot.left) and 
            self.isSubtree(root.right, subRoot.right))
        else:
            self.isSubtree(root.right, subRoot.right)
            self.isSubtree(root.left, subRoot.left)
        """


        