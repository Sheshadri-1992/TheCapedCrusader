#!/usr/bin/env python
import math
import sys

def readInput(filename):

	f = open(filename,'r')
	matrix = []
	for line in f:		
		matrix.append(line.split())

	return matrix

#Find the subtraction factor
def findK(matrix,row,i):

	k = float(matrix[row][i])/float(matrix[i][i])	
	return k

#Solve all the individual levels to 0
def solveCol(matrix,i,choice):

	if(choice==1):
		for row in range(i+1,len(matrix)):			
			k = findK(matrix,row,i)		
			bigRow = map(lambda x : x*k, matrix[i])		
			newList = map( lambda x,y: x-y, bigRow,matrix[row])
			matrix[row] = newList
	else:
		for row in range(i-1,-1,-1):			
			k = findK(matrix,row,i)
			bigRow = map(lambda x : x*k, matrix[i])		
			newList = map( lambda x,y: x-y, bigRow,matrix[row])
			matrix[row] = newList
		
	return matrix

#Solve all the column levels to 0
def solve(matrix,choice):

	if choice==1:
		for i in range(0, len(matrix)-1):
			matrix = solveCol(matrix,i,choice)
	else:
		for i in range(len(matrix)-1,0,-1):
			matrix = solveCol(matrix,i,choice)

	return matrix

#Solve for x1,x2,x3...
def algo(filename):

	myList = readInput(filename)
	
	newList = []
	for i in range(0,len(myList)):
		row = []
		for j in range(0,len(myList[i])):			
			row.append(float(myList[i][j]))

		newList.append(row)

	augmentRow = newList[0]
	
	newList.remove(newList[0])
	newList.pop()

	for i in range(0,len(augmentRow)):
		newList[i].append(augmentRow[i])	

	#End of 1st pass, lower order matrix should  be 0
	result = solve(newList,1)

	print "Output is "
	passNext = []
	for i in range(0,len(result)):
		x = map(lambda y: round(y,3), result[i])

		nList = []
		for j in range(0,len(x)):
			temp = x[j]/x[i]
			nList.append(round(temp,3))

		print nList
		passNext.append(nList)

	#End of 2nd pass, higher order matrix should be 0
	result = solve(passNext,2)
	
	for i in range(0,len(result)):
		row = map(lambda y: math.floor(y), result[i])
		print row

#Start your program here
if len(sys.argv)==0:
	exit()

algo(sys.argv[1])