from fileinput import close
from pickle import FALSE


class Solution():
    def isValid(self, s) -> bool:
        if not(len(s) % 2 == 0):
            return False
        
        stack = []

        close_to_open = {"]": "[", "}": "{", ")": "("}

        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)
        
        if not(stack):
            return True
        else:
            return False
        
test = Solution()
print(test.isValid("()[]{}"))
