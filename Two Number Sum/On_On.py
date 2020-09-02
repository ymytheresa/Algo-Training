def twoNumberSum(array, targetSum):
    # Write your code here.
	for num in array:
		target = targetSum - num
		if target in array and target != num: 
			return [num, target]
	return []
	
	
