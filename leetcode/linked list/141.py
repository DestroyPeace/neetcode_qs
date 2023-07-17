class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode):
        """FLOYD'S TORTOISE AND HARE ALGORITHM

        BECAUSE TWO POINTERS MOVING AT DIFFERENT SPEEDS MEET UP AT SOME POINT, 
        THAT MEANS THERE MUST HAVE BEEN A RESET IN SOME WAY - IN THIS CASE AS A CYCLE:
            
            O(N) TIME COMPLEXITY.
            O(1) TIME COMPLEXITY.

        REASONING:
            Due to the fast pointer moving at twice the speed of the slow pointer,
            this means that the gap betweeen the fast pointer and slow decrease 
            per iteration (imagining the fact that the fast pointer is chasing the slow pointer)
            This means that the time complexity is n because the gap closes at n - 1 each time.
        """

        slow, fast = head, head

        while fast.next: 
            slow, fast = slow.next, fast.next.next

            if slow == fast:
                return True

        return False