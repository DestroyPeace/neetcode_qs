List = list 

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        # All of these values will be used for later comparisons to ensure that the list can be used.
        t1, t2, t3 = target 
        res_triplet = []

        for triplet in triplets:

            # Remove said triplet.
            if not(triplet[0] > t1 or triplet[1] > t2 or triplet[2] > t3):
                res_triplet.append(triplet)

        rt1, rt2, rt3 = 0, 0, 0

        for triplet in res_triplet:
            rt1 = max(triplet[0], rt1)
            rt2 = max(triplet[1], rt2)
            rt3 = max(triplet[2], rt3)
        
        if rt1 == t1 and rt2 == t2 and rt3 == t3:
            return True    

        return False

test = Solution()
print(test.mergeTriplets(triplets = [[3,4,5],[4,5,6]], target = [3,2,5]))