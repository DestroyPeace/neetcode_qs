
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):

        values = {
            
        }
        # 2 PASSES - 1 FOR CLONING, 1 FOR POINTING
        dummy = Node(head)

        while head:
            dummy.val = head.val
            values[dummy.val] = [[head.next, head.random]]
            head = head.next
            dummy = dummy.next

        for value in values:
            dummy.next = values[value][0]
            dummy.random = values[value][1]

            dummy = dummy.next

        return dummy        
