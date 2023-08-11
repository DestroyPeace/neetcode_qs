import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        nums = [num * -1 for num in nums]
        # Creating a min heap that acts like a max heap (negative min heap)
        heapq.heapify(nums)
        print(nums)

        # Iterating through the max heap

        # Identify which layer of the heap you will be looking through by knowing that each layer 
        # increases by a power of 2.

        return nums[k] * -1

        

        

test = Solution()
print(test.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))