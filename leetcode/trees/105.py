# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: int, inorder: int) -> TreeNode:

        """
        DEFINITIONS:

            Preorder:
                Start at the root, go to the left subtree and do preorder on it.
                Then go onto the right subtree and then do preorder subtraversal on it.

                Simple definition is:
                    Root, Left, Right

            Inorder:
                Goes in order of the values ascending. This means that
                you start at the lowest value which is the left-most value, go to the
                parent and then go to the right.

                Simple definition is:
                    Left, Root, Right

                e.g any value before the root is on the left side and any value 
                on the right of the root is on the right side of the root in the tree.
        """

        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)

        # Working on the left hand side by removing all of the values up to the middle 
        # because end point is non inclusive. Then we do the same for mid, going up to 
        # mid because we know all the left values are on the left side of the root.
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

        