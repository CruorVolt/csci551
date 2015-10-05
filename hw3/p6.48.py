#!/usr/bin/python
import random

def findAscDescSubSeq(list):
	ascending = -1#Flag for sequence direction. 1 for asc, 0 for desc, -1 for neither
	ascIndex = -1
	descIndex = -1
	
	bestAscIndex = -1
	bestDescIndex = -1
	
	bestAscLength = 0
	bestDescLength = 0
	
	for i in range(1, len(list)):
		#List is currently ascending
		if list[i] > list[i-1]:
			#handle ascending sequence
			if ascending == 0 or ascending == -1: #we've found a new ascending sequence
				ascIndex = i-1
				
				if descIndex != -1: #If this is the end of a descending sequence
					seqLength = i - descIndex
					if seqLength > bestDescLength:
						bestDescLength = seqLength
						bestDescIndex = descIndex
					
					descIndex = -1#No longer tracking a descending sequence
					
			ascending = 1
		elif list[i] < list[i-1]:
			#handle descending sequence
			if ascending == 1 or ascending == -1: #we've found a new descending sequence
				descIndex = i-1
				
				if ascIndex != -1: #If this is the end of an ascending sequence
					seqLength = i - ascIndex - 1
					if seqLength > bestAscLength:
						bestAscLength = seqLength
						bestAscIndex = ascIndex
					
					ascIndex = -1#No longer tracking an ascending sequence
					
			ascending = 0
		else:#Sequence repeats
			if descIndex != -1: #If this is the end of a descending sequence
					seqLength = i - descIndex
					if seqLength > bestDescLength:
						bestDescLength = seqLength
						bestDescIndex = descIndex
					
					descIndex = -1#No longer tracking a descending sequence
		
			if ascIndex != -1: #If this is the end of an ascending sequence
					seqLength = i - ascIndex - 1
					if seqLength > bestAscLength:
						bestAscLength = seqLength
						bestAscIndex = ascIndex
					
					ascIndex = -1#No longer tracking an ascending sequence
			
			
			ascending = -1
	
	print "Longest Ascending Sequence Index: %d" % bestAscIndex
	print "Longest Ascending Sequence Length: %d" % bestAscLength
	print "Longest Descending Sequence Index: %d" % bestDescIndex
	print "Longest Descending Sequence Length: %d" % bestDescLength
	
	
######################################
test = list()
length = 10
for i in range(0, length):
	new = random.randrange(0, 100)
	test.append(new)
	print "%d" % new ,
print ""
findAscDescSubSeq(test)