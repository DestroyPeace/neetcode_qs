List = list 

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        res = 0

        people.sort()

        while l <= r: 
            print(l, r)
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
                res += 1

            # Assume carry one for the heavy guy.
            else: 
                res += 1
                r -= 1

        return res 
    
test = Solution()
print(test.numRescueBoats(people = [3,2,2,1], limit = 3))

            

