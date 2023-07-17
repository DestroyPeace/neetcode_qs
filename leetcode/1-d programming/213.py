class Solution:
    def rob(self, nums: int) -> int:
        def house_rob(houses):
            rob_1, rob_2 = 0, 0

            for house in houses:

                # Calculating maximum possible number in a 3 wide window. (accounting 
                # for any previous mistakes by calculating the highest value now.)
                temp = max(rob_1 + house, rob_2)

                # Iterating now.
                rob_1 = rob_2 
                rob_2 = temp

            return rob_2 

        if not nums: 
            return 0
        
        if len(nums) == 1:
            return nums[0]


        return max(house_rob(nums[:-1]), house_rob(nums[1:]))


test = Solution()
print(test.rob([2, 3, 2]))
