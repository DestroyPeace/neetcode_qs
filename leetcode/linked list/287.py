class ListNode():
    def __init__(self, val: 0, next = None):
        self.val = val
        self.next = next
    



class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """# CREATE OUR LINKED LIST
        head = ListNode(nums[0])
        
        # CREATING A NODE FOR EACH ELEMENT
        for num in nums:
            head.next = ListNode(nums[num])
            head = head.next
    
        # ITERATE THROUGH EACH OF THE NODES USING FLOYD'S TORTOISE AND HARE ALGO
        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

            if slow == fast:
                return slow.val"""

        slow, fast = 0, 0

        # DO WHILE LOOP
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
    
        # PHASE 2: ADVANCING BOTH THE SLOW AND SLOW2 POINTERS UNTIL THEY MEET : 
        # BASICALLY, WE'RE FINDING THE INDEX TO FIND WHEN THE CYCLE BEGINS. 
        # WE'VE FOUND THE DIFFERENCE BETWEEN THEM, NOW WE JUST NEED TO FIND WHERE THEY MEET
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow

