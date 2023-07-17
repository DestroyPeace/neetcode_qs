class Solution:
    def search(self, nums: list[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        
        while high >= low:
            mid = (high + low) // 2
            
            if nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid
            else:
                return mid
        
        return -1
        