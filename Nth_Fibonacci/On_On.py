# O(n) time | O(n) space
def getNthFib(n, memoize={1:0, 2:1}):
    # Write your code here.
	if n in memoize:
		return memoize[n]
	else:
		memoize[n] = getNthFib(n-2) + getNthFib(n-1)
		return memoize[n]
'''
Time : O(n)
	getting from hashtable is constant time operation 
Space : O(n)

Learnt :
	Repeatative recursion : use hashtables / some ways to store the result for reusing
	could reduce the time complexity
'''