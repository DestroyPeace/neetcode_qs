class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        array = [1]

        for i in range(0, len(nums) - 1):
            array.append(nums[i] * array[i])

        array.append(1)

        for i in range(len(nums) -1, 0, -1):
            array.append(array[len(nums) * 2 - i - 1] * nums[i])

            """rray.append(nums[(i + 1) * -1] * array[len(nums) + i - 1])"""
            print(f"rp - {array} - nums - {nums}")
        
        for i in range(len(nums) * 2 - 1):
            array[i] = array[i] * array[-(i + 1)]

        for _ in range(len(nums)):
            array.pop()

        return(array)
            

        """
        lp = [1]
        rp = [1 for _ in range(len(nums))]

        for i in range(0, len(nums) - 1):
            lp.append(nums[i] * lp[i])
            print(f"lp - {lp}")

        for i in range(len(nums) - 2, -1, - 1):
            rp[i] = nums[i + 1] * rp[i + 1]
            print(f"rp - {rp}")
        
        products = []
        for i in range(len(rp)):
            products.append(lp[i] * rp[i])
        
        return products
        """

test = Solution()
print(test.productExceptSelf([1, 2, 3, 4]))

        
# Things to test:
"""
1) Does storing range(len(nums)) in a variable save any time.
2) Does creating a list waste any time?


"""
