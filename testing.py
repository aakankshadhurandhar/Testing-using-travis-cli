
N = 3


def getMin(arr): 
	
	minInd = 0
	for i in range(1, N): 
		if (arr[i] < arr[minInd]): 
			minInd = i 
	return minInd 

 
def getMax(arr): 

	maxInd = 0
	for i in range(1, N): 
		if (arr[i] > arr[maxInd]): 
			maxInd = i 
	return maxInd 

 
def minOf2(x, y): 

	return x if x < y else y 

 
def minCashFlowRec(amount): 

	
	mxCredit = getMax(amount) 
	mxDebit = getMin(amount) 

	
	if (amount[mxCredit] == 0 and amount[mxDebit] == 0): 
		return 0

	# Find the minimum of two amounts 
	min = minOf2(-amount[mxDebit], amount[mxCredit]) 
	amount[mxCredit] -=min
	amount[mxDebit] += min

	# If minimum is the maximum amount to be 
	print("Person " , mxDebit , " pays " , min
		, " to " , "Person " , mxCredit) 

	
	minCashFlowRec(amount) 


def minCashFlow(graph): 

	# Create an array amount[], 
	# initialize all value in it as 0. 
	amount = [0 for i in range(N)] 

	
	for p in range(N): 
		for i in range(N): 
			amount[p] += (graph[i][p] - graph[p][i]) 

	minCashFlowRec(amount) 
	

graph = [ [0, 1000, 2000], 
		[0, 0, 5000], 
		[0, 0, 0] ] 

minCashFlow(graph) 


