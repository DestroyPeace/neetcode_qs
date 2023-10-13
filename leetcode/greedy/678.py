class Solution:
    def checkValidString(self, s: str) -> bool:
        left, star = 0, 0

        for char in s:
            if char == "(":
                left += 1
            elif char == "*":
                star += 1

            # Dealing with ) by first checking a left is able to be used.
            else:
                if left:
                    left -= 1
                elif star:
                    star -= 1
        
        # All of the right has been removed. 
        while left:
            print(left, star)
            if star:
                left -= 1
                star -= 1
            else:
                return False

        return True 
    
        # If there

test = Solution()
print(test.checkValidString(s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())")) 
