List = list

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # BASE CASE - TOO SMALL TO OVERLAP 
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)

                return res + intervals[i:]

            
            # BSAE CASE - TOO BIG TO OVERLAP. 
            elif newInterval[0] > intervals[i][-1]:
                res.append(intervals[i])
            
            # OVERLAPPING
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][-1])]

        res.append(newInterval)
        return res 

