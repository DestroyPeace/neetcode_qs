from collections import Counter

List = list 

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False 
        
        c = Counter(hand) 

        # Starting from the min each time. 
        
        # NO. of groups made.
        for _ in range(len(hand) // groupSize):
            start = min(c)
            c[start] -= 1

            if c[start] <= 0:
                del c[start]
            
            for i in range(1, groupSize):
                if start + i in c:
                    c[start + i] -= 1

                    if c[start + i] <= 0:
                        del c[start + i]
                else:
                    return False
            
        return True 
    
test = Solution()
print(test.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))

