class Solution:
    def checkValidString(self, s: str) -> bool:
        left, star = [], []

        for index, char in enumerate(s):
            if char == "(":
                left.append(index)
            
            elif char == ")":

                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False 
        
            else:
                star.append(index)
            
        while left and star:
            if left[-1] > star[-1]:
                return False 

            left.pop()
            star.pop()
            
        return len(left) == 0
    
        # If there

test = Solution()
print(test.checkValidString(s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())")) 
