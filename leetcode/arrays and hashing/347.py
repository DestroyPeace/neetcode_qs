class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        f = {}

        for num in nums:
            if num in f:
                f[num] += 1
            else:
                f[num] = 1

        fa = [[] for _ in range(len(nums)+ 1)]
        ans = []

        for i, v in f.items():
            fa[v].append(i)
        
        test = list(filter(([]).__ne__, fa))

        for i in range(1, k + 1):
            for n in test[-1 * i]:
                ans.append(n)
                
                if len(ans) == k:
                    return ans
        # O(n^2)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # O(n)




test = Solution()

print(test.topKFrequent([4,1,-1,2,-1,2,3], 2))