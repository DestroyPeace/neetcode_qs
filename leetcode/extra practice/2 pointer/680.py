class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        removed = False 
        s = list(s)

        # First checking if it's a palindrome:
        if s[::-1] == s:
            return True

        # Finding the first character
        while not removed: 
            print(l, s[l], s[r], r)
            if s[l] != s[r] and not removed: 
                removed = True 

                # Identifying where to move:
                if l + 1 in range(len(s)) and s[l + 1] == s[r]:
                    print("removed", [(i, j)  for i, j in zip("".join(s), "".join(s[::-1]))])
                    s.pop(l)
                
                else:
                    s.pop(r)
            
            if s[l] == s[r]:
                l += 1
                r -= 1
            
        return s[::-1] == s

test = Solution()
print(test.validPalindrome(s =
"aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))