List = list 

# Initial idea to find the location of the last occurence of each letter
# and to create a dictionary of values. I proceed to merge the intervals together 
# and this allows me to identify the partitions. 

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occurences = {

        }

        for i, v in enumerate(s):
            if v not in occurences:
                occurences[v] = [i]
            
            else:
                occurences[v].append(i)
        
        intervals = []
        res = []
        i = 0

        # Attempt to minimise the first letter

        for letter in occurences:
            intervals.append([occurences[letter][0], occurences[letter][-1]])

        # Finding the overlap in intervals - MERGE INTERVALS essentially
        while i in range(len(intervals)):
            curr = intervals[i]
            i += 1

            for interval in intervals[i:]:
                # New interval that has to be considered
                if interval[0] < curr[-1] and interval[0] > curr[0]:
                    curr[-1] = max(interval[-1], curr[-1])
                    i += 1
                else:
                    break
            
            res.append(curr)
        
        # Converting to the lengths of the intervals.
        for i in range(len(res)):
            res[i] = res[i][-1] - res[i][0] + 1
        
        return res
        

test = Solution()
print(test.partitionLabels(s = "eccbbbbdec"))