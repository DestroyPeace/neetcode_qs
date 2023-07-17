class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)

        l, r = dummy, head

        while n > 0 :
            right = right.next
            n -= 1

        # ITERATING BOTH
        while r:            
            l, r = l.next, r.next

        l.next = l.next.next
        return dummy.next

        