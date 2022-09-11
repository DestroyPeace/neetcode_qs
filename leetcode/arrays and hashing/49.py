"""class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in seen:
                seen[sorted_word].append(word)
            else:
                seen[sorted_word] = [word]

        return [value for value in seen.values()]

test = Solution()

print(test.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = collections.defaultdict(list)

        for w in strs:
            count = [0] * 26

            for c in w:
                count[ord(c) - ord(a)] += 1
            ans[tuple(count)].append(w)
            return ans.values()

            

test = Solution()

print(test.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))