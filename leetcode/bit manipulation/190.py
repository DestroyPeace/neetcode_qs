class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            
            # Moving the desired bit to the end to essentially perform an and operation on all of the values?
            bit = (n >> i) & 1

            res |= (bit << (31 - i))

        return res
    
print(Solution().reverseBits(0b00000010100101000001111010011100))