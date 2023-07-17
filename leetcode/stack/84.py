class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        [5,5,1,7,1,1,5,2,7,6] - gives the wrong answer; maybe use a different mathmetical concept by calculating the area gain
        min_n = min(heights)
        max_area = min_n * len(heights)

        l, r = 0, len(heights) - 1

        while l < r:
            print(l, r, max_area, heights[l:r + 1])
            if heights[l] <= heights[r]:
                l += 1

            else:
                r -= 1

            max_area = max(max_area, min(heights[l:r + 1]) * len(heights[l:r + 1]))
            
        return max_area"""
        
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i       
            while stack and h < stack[-1][1]:
                index, height = stack.pop()

                max_area = max(max_area, height * (i - index))
                start = index
            
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area

test = Solution()
print(test.largestRectangleArea([5,5,1,7,1,1,5,2,7,6]))