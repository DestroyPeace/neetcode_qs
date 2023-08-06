class Solution:
    def reverseBits(self, n: int) -> int:
        # CONVERTING N INTO BINARY
        reversed_n = "".join(reversed(bin(n)[2:]))

        return int(reversed_n, base = 2)
    
print(Solution().reverseBits(0b00000010100101000001111010011100))