class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res, l = 0, 0

        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            
            res = max(l - r, res)

        return res


