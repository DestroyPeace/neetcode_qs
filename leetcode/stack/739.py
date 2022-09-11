class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while len(stack) != 0 and t > stack[-1][0]:
                print(stack)
                stack_temp, stack_index = stack.pop() # Getting rid of the lower value

                res[stack_index] = (i - stack_index)

            stack.append([t, i])

        for t, i in stack:
            res[i] = 0

        return res        

test = Solution()
print(test.dailyTemperatures([73,74,75,71,69,72,76,73]))