List = list 

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2: 
            return True 

        l, r = 0, 1
        max_seen = float("-inf")
        passed = False 

        while r < len(nums): 
            if (nums[l] > nums[r]) and passed:
                return False 
            elif (nums[l] > nums[r]):
                passed = True

                # Changing it to be 1 more than the max
                nums[r] = max_seen + 1
            
            max_seen = max(nums[r], max_seen)
            l += 1
            r += 1
    
        return True 
    
test = Solution()
print(test.checkPossibility(nums = [3,4,2,3]))