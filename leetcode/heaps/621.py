import heapq
import math 

from collections import deque, Counter

List = list

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]

        heapq.heapify(maxHeap)

        time = 0 

        q = deque() # pairs of [-cnt, IdleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)

                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

        """queue = deque() # [ [count, res_number_when_to_come_back], ...]
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
        max_heap = [[hash_set[k] * -1, 0, k] for k in hash_set]

        heapq.heapify(max_heap) 

        # Running through the algo now. 
        while max_heap or queue:
            

            # Checking if there are any queues to go through:
            if queue and res == queue[0][1] + 1:
                timer, delay, letter = queue.popleft()

                if timer != 0:
                    heapq.heappush(max_heap, [timer, delay, letter])
                


            # Now, we check the biggest iterable in the max heap

            if max_heap:
                timer, delay, letter = heapq.heappop(max_heap)

                # Letter has been reached.
                if timer == 0:
                    res += 1
                    continue 
                
                print(letter)

                # Checking if it even needs to be added.
                if int(timer) + 1 == 0:
                    res += 1
                    continue 

                # Decreasing the counter by 1 because of -(timer - 1) becoming - timer + 1.
                queue.append([int(timer) + 1, res + n, letter]) 

                res += 1
                continue
            
            if not(max_heap or queue):
                return res 
            
            # Assuming nothing was done.
            res += 1

        return res """
        

test = Solution()
print(test.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2))
