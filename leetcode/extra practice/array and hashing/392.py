"""from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Creating an array of all of the letters present.
        res = []

        for letter in t:
            if letter in s:
                res.append(letter) 
        
        # Using a sliding window to check now.

        l, r = 0, len(s)

        while r in range(len(res) + 1):
            if "".join(res[l: r]) == s:
                return True 
    
            l += 1
            r += 1
        
        return False
        
test = Solution()
print(test.isSubsequence(s = "axc", t = "ahbgdc"))"""


import matplotlib.pyplot as plt

def retire(monthly, rate, terms):
	savings = [0]
	base = [0]
	m_rate = rate / 12

	for i in range(terms):
		base += [i]
		savings += [savings[-1] * (1 + m_rate) + monthly]

def display_retire_monthlies(monthlies, rate, terms):
	plt.figure("retireMonth")
	plt.clf()

	for monthly in monthlies:
		xvals, yvals = retire(monthly, rate, terms)
		plt.plot(xvals, yvals, label = f"retire{str(monthly)}")
		plt.legend(loc = "upper left")

	plt.show()

display_retire_monthlies([500, 600, 700, 800, 900, 1000, 1100], 0.05, 40 * 12)