import collections

class Solution():
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2) or len(s2) == 0:
            return False

        r1, r2 = collections.defaultdict(), collections.defaultdict()

        l = 0

        for c in s1:
            r1[c] = r1.get(c, 0) + 1
        
        for c in s2[l:len(s1)]:
            r2[c] = r2.get(c, 0) + 1
        

        if r1 == r2:
            return True

        for r in range(len(s1), len(s2)):
            l += 1
            i = r - len(s1)
            r2[s2[i]] = r2.get(s2[i], 0) - 1


            r2[s2[r]] = r2.get(s2[r], 0) + 1

            if r1.items() <= r2.items():
                return True

        return False

test = Solution()
print(test.checkInclusion("ab","eidbaooo" ))
            
            
            