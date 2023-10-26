List = list

from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.pts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:

            # SECOND and THIRD conditions are due to the square having to have a positive area.
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue

            if (px, y) in self.pts and (x, py) in self.pts:
                res += self.pts[(x, py)] * self.pts[(px, y)] * self.pts[(x, y)]

        return res


        

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)