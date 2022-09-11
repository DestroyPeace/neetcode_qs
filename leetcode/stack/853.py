"""
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.
"""

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """stack = [[] * len(position)]
        res = []

        for i in range(len(position)):
            new_position = position[i] + speed[i]
            
            if new_position in stack:
                stack.append([new_position, speed[i]])

            else:
                stack.append()"""
        
        if len(position) == 1:
            return 1

        stack = []
        res = []

        for i in range(len(position)):
            stack.append([position[i], speed[i]])
        
        for pos in sorted(stack, key = lambda x: x[0])[::-1]:
            time = (target - pos[0]) / pos[1]
            print(pos, time)

            if res and res[-1] >= time:
                slowest_time = max(res[-1], time)
                res.pop() 
                res.append(slowest_time)
            else:
                res.append(time)

        return len(res)


10
[0,4,2]
[2,1,3]
test = Solution()
print(test.carFleet(target = 10, position = [0,4,2], speed = [2,1,3]))