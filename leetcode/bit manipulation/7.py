class Solution:
    def reverse(self, x):
        
        MIN = -2 ** 31
        MAX = 2**31 - 1

        res = 0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            # OVERFLOW CHECKING BY CHECKING IF IT'S GREATER THAN 
            if (res > MAX // 10 or
                (res == MAX // 10 and digit > MAX % 10)):
                return 0

            # UNDERFLOW CHECKING
            if (res < MIN // 10 or
                (res == MIN // 10 and digit < MIN % 10)):
                return 0
            
            res = (res * 10) + digit
        
        return res
