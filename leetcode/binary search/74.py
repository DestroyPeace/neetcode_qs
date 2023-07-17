

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        high = len(matrix) - 1
        low = 0

        # BINARY SEARCH FOR THE ARRAY IT'S IN
        while high >= low:
            mid = (high + low) // 2

            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][-1] < target:
                low = mid + 1
            else:
                break
        
        arr_high, arr_low = len(matrix[mid]) - 1, 0

        # BINARY SEARCH FOR THE INDEX NOW
        while arr_high >= arr_low: 
            arr_mid = (arr_high + arr_low) // 2
            value = matrix[mid][arr_mid]

            if value > target:
                arr_high = arr_mid - 1
            elif value < target:
                arr_low = arr_mid + 1
            else:
                return True

        return False

test = Solution()
print(test.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))