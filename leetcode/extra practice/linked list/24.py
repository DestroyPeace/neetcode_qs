# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""

import heapq
import collections 
import math

List = list         
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        dummy = ListNode(0, head) 
        prev, curr = dummy, head 

        # Ensuring there are at least two nodes that are able to be reversed. 
        while curr and curr.next: 
            pair = curr.next.next
            second = curr.next 

            # Reverse the order
            second.next = curr 
            curr.next = pair 

            prev.next = second  
            
            # Update the pointers

            prev = curr
            curr = pair 
        
        return dummy.next


        



        
test = Solution()
