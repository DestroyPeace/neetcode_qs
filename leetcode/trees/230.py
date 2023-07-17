# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Saving time by not completing the full list - stopping when we reach 
        # n == k
        n = 0

        # Iterative DFS - Using a pointer to check the current node.
        curr = root
        stack = []

        while curr or stack:

            # Finding the left-most value
            while curr:
                stack.append(curr)
                curr = curr.left

            # Going back to the previous lowest value to check for the right values.
            # As we're going through the lowest values now, we can increment the 
            # counter n.
            curr = stack.pop()
            n += 1

            # If the counter is the same, return the value.
            if n == k:
                return curr.val

            # Moving the pointer to the right most node - then the while loop initiates
            # and forces the pointer to the left-most node of the latest right child.
            curr = curr.right