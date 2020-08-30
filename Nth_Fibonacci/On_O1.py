# O(n) time | O(1) space
def getNthFib(n):
	store = [0,1]
	counter = 3
	while counter <= n:
			result = store[0] + store[1]
			store[0] = store[1]
			store[1] = result
			counter += 1
	return store[1] if n > 1 else store[0]

'''
Learn :
	when i was reading the question : solve the problem by thinking the 'meaning' 
	of the question. -> solve it by explaining the question
	
	But to optimise time -> I should think of constant operations -> that way I could relate to
	get() for hashtables
	
	To optimise space -> I should think : what type of data are needed 
	-> last last result + last result always
	-> then simply storing these 2 values would be enough
	
	Try : think the question -> any constant time operations ? -> what data should be stored ? 
'''