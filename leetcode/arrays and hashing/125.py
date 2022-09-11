"""
class Solution:
    def isPalindrome(self, s):
        a = "".join(i for i in s if i.isalnum()).lower()
        
        return a == a[::-1]

test = Solution()

print(test.isPalindrome("A man, a plan, a canal: Panama"))
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "".join(i for i in s if i.isalnum()).lower()
        l = 0
        r = len(a) - 1

        while l < r:
            if a[l] == a[r]:
                l += 1
                r -= 1
           
            else:
                return False

        return True
        
test = Solution()

print(test.isPalindrome("A man, a plan, a canal: Panama"))