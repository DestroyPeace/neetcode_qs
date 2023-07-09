# Interleaving String

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]


        """if len(s3) != (len(s1) + len(s2)):
            return False

        values = []

        s1, s2 = list(s1), list(s2)

        # Initial idea is to brute-force it?
        def dfs(index, string_1 = s1, string_2 = s2, total = []):
            if len(total) == len(s3):
                values.append(total)

            if index not in range(len(s3)):
                return False

            t_letter = s3[index] 
            
            if (string_1 and t_letter == string_1[0]) and (string_2 and t_letter == string_2[0]):
                # TWO OPTIONS: BRUTE FORCE BOTH?

                dfs(index + 1, string_1[1::], string_2[::], total[::] + [string_1[0]])
                dfs(index + 1, string_1[::], string_2[1::], total[::] + [string_2[0]])
        
            elif string_1 and t_letter == string_1[0]:
                val_s1 = string_1.pop(0)

                total.append(val_s1)

                dfs(index + 1, string_1[::], string_2[::], total[::])
            
            elif string_2 and t_letter == string_2[0]:
                val_s2 = string_2.pop(0)
                total.append(val_s2)

                dfs(index + 1, string_1[::], string_2[::], total[::])

        dfs(0, s1, s2)

        if values:
            return True 
        else:
            return False"""

test = Solution()
print(test.isInterleave(s1 = "", s2 = "", s3 = ""))