'''https://leetcode.com/problems/paint-house/description/'''

def minCost(self, costs: List[List[int]]) -> int:
	numDays = len(costs)
	memo = {}
	
	def dfs(i, prev):
		if i == numDays:
			return 0
		elif (i, prev) in memo:
			return memo[(i, prev)]
		
		best = float('inf')
		for colorIdx, cost in enumerate(costs[i]):
			if colorIdx == prev:
				continue

			best = min(best, cost + dfs(i + 1, colorIdx))
		
		memo[(i, prev)] = best
		
		return best
		
	return dfs(0, -1)