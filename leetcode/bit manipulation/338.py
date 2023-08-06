class Solution:
    def countBits(self, n: int) -> list[int]:
        res_array = []



        """
        SLOW METHOD - FIRST METHOD

        BEAT 28% OF PEOPLE.
        
        def num_of_1_bits(den_num):
            res = 0

            while den_num:
                res += den_num % 2

                den_num >>= 1

            return res 
        

        for num in range(0, n + 1):
            res_array.append(num_of_1_bits(num))

        return res_array
"""


        """
        FAST DP METHOD - BEAT 99% OF PEOPLE
        
        dp = [0] * (n + 1)
        ans = [0]

        offset = 1
        for i in range(1, n + 1):
            
            # Ensure each time you double the value of the offset.
            if offset * 2 == i:
                offset = i

            dp[i] = 1 + dp[i - offset
        return dp"""

test = Solution()
print(test.countBits(7))