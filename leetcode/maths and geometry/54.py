List = list 

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)

        while l < r and t < b:
            
            # Get every index in the top row
            # Right goes out of bounds.
            for i in range(l, r):
                res.append(matrix[t][i])

            t += 1
            
            # get every i in the right column

            for i in range(t, b):
                res.append(matrix[i][r - 1])

            r -= 1

            if not (l < r and t < b):
                break
                
            # Getting every i in the bottom row
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            
            b -= 1

            # Getting every i in the left row
            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])

            l += 1

        return res 
    
test = Solution()


