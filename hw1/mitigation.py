import copy
import math

def col_distance(a):
	score = 0
	for i in range(0, len(a)):
		for j in range(0, len(a)):
			for k in range(1, len(a)-j):
				#print("%d:%d" % (a[i][j], a[i][j+k]))
				score += abs(a[i][j]-a[i][j+k])
	#print("Total Score: %d" % score)
	return score
	
def check_square(a):
	if sqrt(a) - floor(sqrt(a)) != 0:
		return 0
	return 1
	
def doubleRow(a, rowIndex):
	b = COPY_PLEASE(a)
	for i in range(0, len(b)):
		b[i][rowIndex] *= 2
	return b
	
def decrementColumn(a, columnIndex):
	for i in range(0, len(a)):
		a[columnIndex][i] -= 1
	return a
	
def colContainsOne(a, columnIndex):
	for i in range(0, len(a)):
		if a[columnIndex][i] == 1:
			return 1
	return 0
	
def zero(a):
	global z
	#if !check_square(a):
	#	print "Input not square"
	#	exit()
	#newA = [sqrt(a)]
	#for i = 0
	currentScore = col_distance(a)
	index = [-1]
	score = [99999999999]
	pickLeastBadDouble(a, index, score)
	
	if score[0] > currentScore:
		unity(a)
		pickLeastBadDouble(a, index, score)
		a = doubleRow(a, index[0])
	else:
		a = doubleRow(a, index)
		
	if isUnity(a) == 0:
		print(a)
		zero(a)
	else:
		print("Unity!")
		
#return the index of the least bad row to double
#index and score return the index and score of the least bad row
def pickLeastBadDouble(a, index, score):
	score[0] = 99999999999
	index[0] = -1
	for i in range(0, len(a)):
		if col_distance(doubleRow(a, i)) < score[0]:
			score[0] = col_distance(doubleRow(a, i))
			index[0] = i
	
#decrement each column until it contains at least one 1
def unity(a):
	for i in range(0, len(a)):
		while(colContainsOne(a, i) == 0):
			decrementColumn(a, i)
			
#check if a is all 1's
def isUnity(a):
	for i in range(0, len(a)):
		for j in range(0, len(a)):
			if a[i][j] != 1:
				return 0
	return 1

#apparently asking python to actually copy something without any references to it is too much to ask for
def COPY_PLEASE(a):
	new = []
	for i in range(0, len(a)):
		new.append([])
		for j in range(0, len(a[0])):
			new[i].append(a[i][j])
			
	return new

z = 0
test = [[3,4,5],[5,8,3],[7,10,2]]
zero(test)