import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        heapq.heapify(nums)

        # Removing all the elements until we are at element k
        while len(nums) > k:
            heapq.heappop(nums)
        
        # Returning the now smallest integer, that will be our kth largest integer.
        return nums[0]
        

        

test = Solution()
print(test.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))