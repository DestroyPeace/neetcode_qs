import heapq
import math 

from collections import deque

List = list

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        queue = deque() # [ [time_till_next_available, delay], ...]
        res = 0 

        # No delay means any letter can be used in any order.
        if n == 0:
            return len(tasks)
        
        # Attempting to build a max heap to ensure the largest element is used.
        hash_set = {
            task: 0 for task in tasks
        }

        # Creating a counter 
        for task in tasks:
            hash_set[task] += 1
        
        # Creating a negative key for which the values are constructed to fit the max heap.
        max_heap = [[hash_set[k] * -1, 0] for k in hash_set]

        heapq.heapify(max_heap) 

        # Running through the algo now. 
        while max_heap or queue:
            # Checking if there are any queues to go through:
            if queue and res == queue[0][1]:
                timer, delay = queue.popleft()

                heapq.heappush(max_heap, [timer, delay])

            # Now, we check the biggest iterable in the max heap

            elif max_heap:
                timer, delay = heapq.heappop(max_heap)

                # Letter has been reached.
                if timer == 0:
                    res += 1
                    continue 

                # Decreasing the counter by 1 because of -(timer - 1) becoming - timer + 1.
                queue.append([int(timer) + 1, res + n]) 

                res += 1
            
            # General case: if none of the conditions are actived, then this is considered an IDLE.
            else:
                res += 1

            print(max_heap, queue, res)

        return res 
        

test = Solution()
print(test.leastInterval(tasks = ["A","A","A","B","B", "C", "C"], n = 1))
