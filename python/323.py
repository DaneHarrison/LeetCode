class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
		parent = {}
		
		def find(x):
			if x != parent[x]:
				parent[x] = find(parent[x])
				
			return parent[x]
		
		def union(x, y):
			xRoot = find(x)
			yRoot = find(y)
			
			if xRoot != yRoot:
				parent[xRoot] = yRoot
		
		for s, e in edges:
			if not s in parent:
				parent[s] = s
			if not e in parent:
				parent[e] = e
			
			union(s, e)
		
		groups = defaultdict(list)
		for node in parent:
			root = find(node)
			groups[root].append(node)
		
		return len(groups.keys())
			