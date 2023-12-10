"""
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
"""

import heapq
import collections 
import math

List = list         

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        if "Y" not in customers: 
            return 0
        elif "N" not in customers:
            return len(customers)

        vals = collections.Counter(customers)

        # Base value assuming we close at the 0th hour. 
        res = [float("inf"), 0]

        closed = 0

        # Penalties = +1 for every hour where a customer isn't present. 
        # Assuming we attempt to close at each of these r values. 
        for r in range(0, len(customers)):
            res = min([[closed + vals["Y"], r], res])

            if customers[r] == "N": 
                closed += 1
            else: 
                vals["Y"] -= 1
            
            # Number of closed during the hour when it's closed as well as 
            # number of customers left to come left out on.

        # Accounting for closing at the very end

        res = min([[closed, len(customers)], res])

        return res[1]


test = Solution()
print(test.bestClosingTime(customers = "YYNY"))
