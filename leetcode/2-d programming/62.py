class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tempRow = [1] * n
        for row in  range(1, m):
            for col in range(1, n):
                # we are using the current col value before reassigning it
                tempRow[col] = tempRow[col - 1] + tempRow[col]
                
            print(tempRow)
        return tempRow[-1]


        """global res
        target = (m - 1, n - 1)
        res = 0

        cache =  []


        def dfs(row, col, prev_coord):
            global res

            if (row, col) in cache:
                res += 1
                return 

            if row not in range(m) or col not in range(n):
                return 

            if (row, col) == target:
                # Long start-up however, might save time later on.
                for row, col in prev_coord:
                    if (row, col) not in cache:
                        cache.append((row, col))

                res += 1
                return

            prev_coord.append((row, col))

            dfs(row + 1, col, prev_coord.copy())
            dfs(row, col + 1, prev_coord.copy())

        dfs(0, 0, [])
        return res """

print(Solution().uniquePaths(7, 3))