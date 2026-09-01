class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
		if len(edges) != n - 1:
			return False
		
		parent = {}
		
		def find(x):
			if x != parent[x]:
				parent[x] = find(parent[x])
				
			return parent[x]
			
		def union(x, y):
			xRoot = find(x)
			yRoot = find(y)
			
			if xRoot == yRoot:
				return False
			
			parent[xRoot] = yRoot
			
			return True
		
		for s, e in edges:
			if s not in parent:
				parent[s] = s
			if e not in parent:
				parent[e] = e
			
			if not union(s, e):
				return False
		
		groups = defaultdict(list):
		for curr in parent:
			root = find(curr)
			groups[root].append(curr)
		
		return len(groups.keys()) == 1