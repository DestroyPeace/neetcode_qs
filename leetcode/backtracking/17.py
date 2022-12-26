class Solution:
    def letterCombinations(self, digits: str) -> str:
        
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghI",
            "5": "jkl",
            "6": "mno", 
            "7": "prqs",
            "8": "tuv", 
            "9": "wxyz"
        }
        
        """res = []

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for character in mapping[digits[i]]:
                backtrack(i + 1, curStr + character)

        if digits:
            backtrack(0, "")
        
        return res
        """


        res = []
        
        def backtrack(index, string):
            if len(string) == len(digits):
                res.append(string)
                string.clear()
                return
            
            print(index)
            for letter in mapping[digits[index]]:
                print(string, mapping[digits[index]])
                string.append(letter)


                # Reached the end of the digits.
                backtrack(index + 1, string.copy())

        if digits:
            backtrack(0, [])

        return res

test = Solution()
print(test.letterCombinations("23"))