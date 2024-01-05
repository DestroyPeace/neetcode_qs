"""
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
"""


import heapq
import collections 
import math

List = list   

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dx, dy = 0, 1

        x, y = 0, 0

        for instruction in instructions: 
            if instruction == "G":
                x, y = x + dx, y + dy 
            
            # When rotating by 90 degrees, you are swapping the x and y values.
            
            elif instruction == "L":
                dx, dy = -dy, dx 
            
            else:
                dx, dy = dy, -dx 

        return (x, y) == (0, 0) or (dx, dy) != (0, 1)
        
test = Solution()
