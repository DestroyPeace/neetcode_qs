class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # REVERSING BOTH LISTS FIRST
        prev, curr = None, l1

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        prev, curr = None, l2

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        val_1, val_2 = [], []

        head_1, head_2 = l1, l2

        while head_1:
            val_1.append(head_1.val)
            head_1 = head_1.next

        while head_2:
            val_2.append(head_2.val)
            head_2 = head_2.next

        sum = str(int(val_1.join()) + int(val_2.join()))
        # CREATING NODES FOR EACH OF THE VALUES

        for n in reversed(sum):
            dummy = ListNode(val = int(n))
            dummy.next = ListNode(val = int())