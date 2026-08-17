'''
Two Train Scheduling

You are given two trains, Train A and Train B. Each train has a sequence of stops that it must visit in order.

Each stop has a travel time to the next stop.

Only one train can be traveling at a time.

You must schedule the trains so that both trains complete their entire routes, minimizing the total amount of time required.

There is one additional constraint:

If the same train travels twice in a row, it must first return to the location where it started its previous trip. The time required to return is given by a returnTime value.

You may alternate between the two trains as often as you want.

Function signature
def minCompletionTime(
    trainA: List[int],
    trainB: List[int],
    returnTime: int
) -> int:

Where:

trainA[i] = time required for Train A to travel from stop i to stop i + 1
trainB[i] = time required for Train B to travel from stop i to stop i + 1
returnTime = time required for a train to return to its starting position before being used again consecutively

Return the minimum total time required for both trains to complete their routes.

Example
trainA = [3, 2, 5]
trainB = [4, 1, 3]
returnTime = 2

Your job is to determine the optimal ordering of the trips between the two trains.
'''

def minCompletionTime(
    trainA: List[int],
    trainB: List[int],
    returnTime: int
) -> int:
	memo = {}
	
	def dfs(i, j, prev):
		if i == len(trainA) and j == len(trainB):
			return 0
		elif (i, j, prev) in memo:
			return memo[(i, j, prev)]
		
		res = float('inf')
		
		# take i
		if i < len(trainA):
			currCost = trainA[i] + (returnTime if prev == 0 else 0)
			res = min(res, currCost + dfs(i + 1, j, 0))
		
		# take j
		if j < len(trainB):
			currCost = trainB[j] + (returnTime if prev == 1 else 0)
			res = min(res, currCost + dfs(i, j + 1, 1))
		
		memo[(i, j, prev)] = res
		
		return res 
	
	return dfs(0, 0, -1)