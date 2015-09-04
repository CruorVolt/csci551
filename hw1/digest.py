width = 0

def partial_digest(L): 
	global width
	width = max(L)
	L.remove(width)
	X = [0, width]
	place(L, X)

def place(L, X):
	global width
	if not L:
		X.sort()
		print(X)
		return
	y = max(L)
	if set(delta(width - y, X)).issubset(set(L)):
		X.append(width - y)
		delete(delta(width-y,X),L)
		place(L,X)
		X.remove(width - y)
		L.extend(delta(width - y, X))
	if set(delta(y,X)).issubset(set(L)):
		X.append(y)
		delete(delta(y,X), L)
		place(L,X)
		X.remove(y)
		L.extend(delta(y,X))
	return
	
#remove list y from L
def delete(y, L):
	for x in y:
		if x in L:
			L.remove(x)

def delta(y, X):
	list = []
	for num in X:
		list.append(abs(y - num))
	return list
	
#4.2
#Solution:
#	[0,3,4,5,6,9,15]
#	[0,6,9,10,11,12,15]
L = [1,1,1,2,2,3,3,3,4,4,5,5,6,6,6,9,9,10,11,12,15]

#Example from algorithm description
#Solution: [0,2,4,7,10]
#L = [2,2,3,3,4,5,6,7,8,10]
partial_digest(L)