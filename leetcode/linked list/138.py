
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        values = {
            None: None
        }
        
        curr = head

        while curr:
            copy = Node(curr.val)
            values[curr] = copy
            curr = curr.next

        curr = head

        while curr:
            copy = values[curr]
            copy.next = values[curr.next]
            copy.random = values[curr.random]

            curr = curr.next

        return values[head]