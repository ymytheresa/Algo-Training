def twoNumberSum(array, targetSum):
    # Write your code here.	
	array.sort() #nlogn
	left = 0
	right = len(array)-1
	while left < right: #at least 1 element
		#worst case = find n times
		# n < nlongn
		# n
		sum = array[left] + array[right]
		if sum == targetSum:
			return[array[left], array[right]]
		elif sum > targetSum:
			right -= 1
		else:
			left += 1
	return []
