import math

"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """min_speed = 0 
        time = 0 

        for k in range(max(piles), 1,  -1):
            for pile in piles:
                time += ceil(pile / k)

            if time > h:
                return min_speed
            else:
                min_speed = k

            time = 0

        return min_speed
        BRUTE FORCE METHOD (O(max(p)n))
        """
        
        """time = 0
        min_speed = float("infinity")

        high = max(piles)
        low = 0
        
        while high >= low:
            mid = (high + low) // 2
            
            for pile in piles:
                time += ceil(pile / mid)
            
            if time < h:
                low = mid + 1
                min_speed = min(min_speed, time)

            elif time > h:
                high = mid - 1

            else:
                print("exact value found")
                print(mid, time, high, low, min_speed)
                return min_speed
                
        return min_speed"""

        l, r = 1, max(piles)                
        min_speed = 0


        while l <= r:
            m = (l + r) // 2
            time = 0

            for pile in piles:
                time += math.ceil(pile / m)
            
            if time <= h:
                min_speed = m
                r = m - 1
            else:
                l = m + 1

        return min_speed


test = Solution()
print(test.minEatingSpeed([3,6,7,11], 8))