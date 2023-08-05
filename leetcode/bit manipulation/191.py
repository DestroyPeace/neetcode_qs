class Solution:
    def hammingWeight(self, n: int) -> int:
        """# MOD SOLUTION
        res = 0 

        while n:
            res += n % 2 # REMOVING THE RIGHTMOST BIT IF IT'S A 1 DUE TO MAKING THE 
                         # VALUE ODD
            
            n >>= 1 # SHIFTING THE VALUES TO THE RIGHT TO MOVE EACH 1 CLOSER TO THE START

        return res"""
        res = 0

        while n:
            print(f"{n} before")
            print("==================")
            n &= (n - 1)
            print(f"{n} after")
            res += 1

        return res
    

test = Solution()
print(test.hammingWeight(11111111111111111111111111111101))