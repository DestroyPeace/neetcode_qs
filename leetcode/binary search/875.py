from math import ceil

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
        
        time = 0
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
                
        return min_speed
                

test = Solution()
print(test.minEatingSpeed([3,6,7,11], 8))