List = list 

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        directions = [[1,0],[-1,0],[0,1],[0,-1],
                      [1,1],[-1,-1],[1,-1],[-1,1]]
        
        board[rMove][cMove] = color 
    
        def legal(row, col, color, direction):
            dr, dc = direction 

            row, col = row + dr, col + dc 

            length = 1

            while row in range(8) and col in range(8):
                length += 1

                if board[row][col] == ".":
                    return False 
                
                if board[row][col] == color: 
                    return length >= 3

                row, col = row + dr, col + dc 
            
            return False 

        for direction in directions: 
            if legal(rMove, cMove, color, direction):
                return True 
        
        return False 
        