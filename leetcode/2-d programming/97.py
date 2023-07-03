# Interleaving String

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        values = []
        # Initial idea is to brute-force it?
        def dfs(index, string_1 = s1, string_2 = s2, total = []):
            t_letter = s3[index] 

            if t_letter in s1 and s2:
                # TWO OPTIONS: BRUTE FORCE BOTH?
                val_s1, val_s2 = s1.pop(), s2.pop()

                dfs(index + 1, s1[::], s2, total[::] + [val_s1])

                dfs(index + 1, s1, s2[::], total[::] + [val_s2])
        
            elif t_letter in s1:
                val_s1 = s1.pop()
                total.append(val_s1)

                dfs(index + 1, s1[::], s2, total[::])
            
            elif t_letter in s2:
                val_s2 = s2.pop()
                total.append(val_s2)

                dfs(index + 1, s1, s2[::], total[::])

            else:
                return 0 


            
            