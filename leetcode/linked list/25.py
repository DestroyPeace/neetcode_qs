# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head) # Initialising node
        group_prev = dummy # Pointer before the start of the group that allows .prev of k1

        while True:
            group_end = self.get_group_end(group_prev, k) # Finding the end of the K group

            # If no group exists, break
            if not group_end:
                break 
            
            group_next = group_end.next

            # Reverse the group.
            prev, curr = group_end.next, group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next # Storing the first node of the group
            group_prev.next = group_end
            group_prev = temp # Changing the first node of the group to be the prev due to reversed list.

        return dummy.next

    def get_group_end(self, curr, k):
        while curr and k > 0:
            curr = curr.next # Iterating thru linked list
            k -= 1
        return curr        