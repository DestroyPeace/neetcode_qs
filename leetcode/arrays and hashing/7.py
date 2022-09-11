class Solution:
    def reverse(self, x):
        if x > 0:
            val = "".join(list(str(x))[::-1])
        else:
            val = "".join(list(str(x))[::-1][:-1])
        
        if int(val) < 2 ** 31 - 1:

            if x >= 0:
                return int(val)
            elif x <= 0:
                return int(val) * -1
        
        return 0
    
test = Solution()
print(test.reverse(-123))