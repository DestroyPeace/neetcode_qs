# To rotate a matrix 90 degrees clockwise, you have to multiple by the matrix:

List = list 

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for row in range(len(matrix)):
            for col in range(row, len(matrix)):
                print(matrix, row, col)
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]

                matrix[col][row] = temp 

        for row in matrix:
            row.reverse()
