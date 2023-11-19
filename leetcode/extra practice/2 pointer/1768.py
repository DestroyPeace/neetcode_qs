class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))

        res = [] 

        for i, j in zip(word1[:min_len + 1], word2[:min_len + 1]):
            res.append(i)
            res.append(j)
        
        if len(word1) > min_len:
            for letter in word1[min_len:]:
                res.append(letter)
        
        elif len(word2) > min_len:
            for letter in word2[min_len:]:
                res.append(letter)

        return "".join(res)