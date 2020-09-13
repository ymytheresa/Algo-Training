def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	arrayOne.sort()
	arrayTwo.sort()
	oneIdx = 0
	twoIdx = 0
	minLeft = arrayOne[0]
	minRight = arrayTwo[0]
	
	while oneIdx < len(arrayOne) and twoIdx < len(arrayTwo):
		if arrayOne[oneIdx] == arrayTwo[twoIdx]:
			return [arrayOne[oneIdx], arrayTwo[twoIdx]]
		elif arrayOne[oneIdx] < arrayTwo[twoIdx] and oneIdx < len(arrayOne)-1:
			oneIdx += 1
		elif arrayOne[oneIdx] > arrayTwo[twoIdx] and twoIdx < len(arrayTwo)-1:
			twoIdx += 1
		
		minDiff = abs(minLeft - minRight)
		newDiff = abs(arrayOne[oneIdx] - arrayTwo[twoIdx])
		if newDiff < minDiff:
			minLeft = arrayOne[oneIdx]
			minRight = arrayTwo[twoIdx]
		

		
	return[minLeft, minRight]
		
		
