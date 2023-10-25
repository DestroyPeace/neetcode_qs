class Solution:
    def isHappy(self, n: int) -> bool:
        
        if n == 1:
            return True 

        visited = [n]

        while True: 
            digits = [int(i) ** 2 for i in str(n)]
            
            res = sum(digits)
            n = res

            if res in visited:
                return False 
            elif res == 1:
                return True 
            else:
                visited.append(res)

test = Solution()
print(test.isHappy(2))