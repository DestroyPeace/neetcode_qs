# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        
        from collections import deque

        deque_p = deque([p])
        deque_q = deque([q])

        while deque_p:
            for _ in range(len(deque_q)):
                node_1 = deque_q.popleft()
                node_2 = deque_p.popleft()

                if node_1 == node_2:
                    deque_p.extend(node_1.left, node_1.right)
                    deque_q.extend(node_2.left, node_2.right)
                else:
                    return False

        return True
        

        """

        # Using cases to prove that the tree is NOT the same rather than testing if
        # it is the same tree.
        if not p and not q:
            return True
        
        if (not p or not q) or (p.val != q.val):
            return False

        # RECURSIVELY GOING THROUGH IT NOW

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))               