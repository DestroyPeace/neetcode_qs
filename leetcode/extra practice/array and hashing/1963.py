class Solution:
    def minSwaps(self, s: str) -> int:
        opened, closed = 0, 0
        swaps = 0

        for bracket in s:
            if bracket == "[":
                opened += 1
            else:
                closed += 1

            if closed > opened:
                swaps += 1
                opened += 1
                closed -= 1 

        return swaps 