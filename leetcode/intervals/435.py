List = list

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # LOGIC IS THAT WHENEVER AN OVERLAP IS DETECTED, REMOVE THE LONGEST LENGTH TO MIMISE 
        # NUMBER OF OVERLAPS. 

        # 3 CONDITIONS: 

        # THEY DON'T OVERLAP: IN WHICH CASE MOVE ON.
        # THEY DO OVERLAP, IN WHICH CASE THERE ARE TH

        intervals = sorted(intervals, key = lambda x: x[0])

        temp_res = intervals[0]
        res = 0

        for i in range(1, len(intervals)):
            # DETECTING AN OVERLAP BY COMPARING LAST TO FIRST NODES OR CHECKING IF THEY SHARE
            # THE SAME STARTING NODE. 

            if intervals[i][0] < temp_res[1] or intervals[i][0] == temp_res[0]:
                # Checking for the interval which ends later.
                if temp_res[1] < intervals[i][1]:
                    # Essentially, we skip this node and remove it, keeping our comparative interval.
                    res += 1
                
                elif temp_res[1] > intervals[i][1]:
                    temp_res = intervals[i]
                    res += 1
                
                # Both intervals are the same.
                else:
                    res += 1
            
            # If no comparison has been made - no overlap detected
            else:
                temp_res = intervals[i]

        return res 

test = Solution()
print(test.eraseOverlapIntervals(intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]))