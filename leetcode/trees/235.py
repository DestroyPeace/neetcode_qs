# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            # Checking if both values are greater than curr, and in a BST, that means the
            # nodes are to the right of the tree.

            if p.val > curr.val and q.val > curr.val:
                curr = curr.right

            # Likewise, the opposite is true in the case of both values being less than the 
            # current value, in which case we switch the pointer to the go the left.

            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left

            # If either node is on either side of the root, that means that this is a split.
            else:
                return curr