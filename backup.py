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
def solveCol(matrix,i):

	print "Solve col"	
	for row in range(i+1,len(matrix)):
		
		k = findK(matrix,row,i)
		print row,",",i, " k is ", k
		bigRow = map(lambda x : x*k, matrix[i])
		
		newList = map( lambda x,y: x-y, bigRow,matrix[row])
		matrix[row] = newList
		print "Hello ",newList

	return matrix

#Solve all the column levels to 0
def solve(matrix):

	augmentRow = matrix[0]
	firstRow = matrix[-1]

	matrix.remove(matrix[0])
	matrix.pop()

	for i in range(0,len(augmentRow)):
		for j in range(0,len(matrix[i])):
			matrix[i][j] = matrix[i][j]

		matrix[i].append(augmentRow[i])	

	# print "The matrix is "
	for ele in matrix:
		print ele  

	for i in range(0, len(matrix)-1):
		matrix = solveCol(matrix,i)

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

	result = solve(newList)

	print "Output is "
	passNext = []
	for i in range(0,len(result)):
		x = map(lambda y: round(y,3), result[i])

		nList = []
		flag = False
		for j in range(0,len(x)):
			temp = x[j]/x[i]
			nList.append(round(temp,3))

		print nList
		passNext.append(nList)

	result = solve(passNext)

if len(sys.argv)==0:
	exit()

algo(sys.argv[1])