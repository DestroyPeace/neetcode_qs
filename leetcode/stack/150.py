import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for c in tokens:
            match c:
                case "+":
                    stack.append(int(stack.pop()) + int(stack.pop()))
                case "-":
                    value_2 = int(stack.pop())
                    value_1 = int(stack.pop())
                    
                    stack.append(value_1 - value_2)
                case "*":
                    stack.append(int(stack.pop()) * int(stack.pop()))
                case "/":
                    value_2 = int(stack.pop())
                    value_1 = int(stack.pop())

                    res = value_1 / value_2
                    stack.append(math.floor(res) if res > 0 else math.ceil(res))
                case _:
                    stack.append(c)

        return stack[0]

test = Solution()
print(test.evalRPN(
["4","3","-"]))
