import sys
import operator

def checkDigit(inputString):
	inputString = inputString.split(" ")
	flag = 0

	for i in inputString:
		if i.isdigit():
			try:
				flag= int(i)
			except ValueError:
				flag = float(i)
			break
			
	return flag

argCount = len(sys.argv)
lineDict = {}
if argCount>3:
	print 'Invalid Arguments. Try Again !!!'
else:
	totalLines = int(sys.argv[1])
	lines = [i.replace("\n","") for i in sys.stdin.readlines()]
	lineIndexDict = {}
	lineDigitDict = {}

	for i in range(len(lines)):
		lineIndexDict[i] = lines[i]
		digit = checkDigit(lines[i])
		lineDigitDict[i] = digit
	# print lineIndexDict
	sorted_x = sorted(lineDigitDict.items(), key=operator.itemgetter(1),reverse =True)
	temp = sorted_x[0][1]
	temp_update = []
	rank = 1
	count = 1
	

	for i in range(0,len(sorted_x)):
		index = sorted_x[i][1]
		if temp != index:
			count = 1
			rank = i + count

		if rank <=totalLines:
			print lineIndexDict[sorted_x[i][0]]
		temp = index
		
