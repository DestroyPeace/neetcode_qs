List = list

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals = sorted(intervals, key = lambda x: x[0])

        # Using the first interval we are given as the starting point.
        temp_res = intervals[0]

        # ESSENTIALLY THE SAME AS 57.PY EXCEPT DO IT FOR EACH INTERVAL 

        i = 0
        while i <= len(intervals):
            # Ensuring that there is a next interval to check.
            # Checking if the minimum is less than the maximum of our temporary result.
            if i <= len(intervals) - 1 and intervals[i][0] <= temp_res[1]:
                # OVERLAPPING CLAUSE 

                temp_res = [min(temp_res[0], intervals[i][0]), max(temp_res[1], intervals[i][1])]
                i += 1

            # NO INTERVAL LEFT MEANS WE CAN APPEND TO RES AND SET THE NEW TEMP_RES EQUAL TO THE CURRENT INTERVAL
            # TO CHECK. 
            else:
                res.append(temp_res)

                if i in range(len(intervals)):
                    temp_res = intervals[i]

                i += 1


        return res 
    
test = Solution()
print(test.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))

            