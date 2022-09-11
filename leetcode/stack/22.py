class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = []

        def backtrack(open, close):
            if open == close == n:
                res.append("".join(stack))
                print(res)
                return 
            
            if open < n:
                print(stack)
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop()
            
            if close < open:
                print(stack)
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()

        backtrack(0, 0)
        return res

test = Solution()
print(test.generateParenthesis(3))