# O(2^n) time | O(n) space
def getNthFib(n):
    # Write your code here.
	if n==1 :
		return 0
	elif n==2 :
		return 1
	else :
		return getNthFib(n-2) + getNthFib(n-1)

'''
Time complexity : O(2^n)
	Everytime we call a function, we call 2 more functions : 1 -> 2 -> 4 -> ...
Space complexity : O(n)
	Recurion, we are using callstack, things return until n=0, n=1. Before returning, things are stored
'''