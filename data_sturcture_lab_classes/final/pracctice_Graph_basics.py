class Graph:
	def __init__(self, N=1000):
		self.N = N
		# Create 2D list M: M[i][j] = 1, if edge (i,j) exists
		self.M = [[0 for _ in range(N)] for _ in range(N)]
	
	def insert_edge(self, v1, v2):
		# this is an undirected graph
		self.M[v1][v2]=1
		self.M[v2][v1]=1
	
	def adjacent_vertices(self, v):
		# return the adjacent (or linked) vertices to v
		vs = []
		for j in range(self.N):
			if self.M[v][j]=1: # 연결되어있으면 vs 리스트에 
				vs.append(j)
		return vs	
	

class DFS:
	def __init__(self, G):
		# Graph Info
		self.G = G
		self.N = G.N
		
		# Vertex and Edge Labels
		# FOR LABELING, use EXACTLY these labels
		self.UNEXPLORED, self.VISITED = 'unxp', 'vstd'
		self.DISCOVERY, self.BACK = 'dscv', 'back'
		
		# Initialize Vertex and Edge Labels 
		self.V_label = [self.UNEXPLORED for _ in range(N)]
		self.E_label = [[self.UNEXPLORED for _ in range(N)] for _ in range(N)]
		
		# Vertex Visiting Order during DFS
		self.visit_order = []
		
		# Run DFS
		for v in range(self.N):
			if self.V_label[v] == self.UNEXPLORED:
				self.dfs(v)
		
	def dfs(self, v):
		self.V_label[v] = self.VISITED # vertex V 방문
		self.visit_order.append(v) # list에 추가
		
		v_adj = self.G.adjacent_vertices(v)
		for w in v_adj:
			if self.E_label[v][w] == self.UNEXPLORED and self.E_label[w][v] == self.UNEXPLORED:
				if self.V_label[w] == self.UNEXPLORED:
					self.E_label[v][w] = self.DISCOVERY
					self.dfs(w)
				else:
					self.E_label[v][w] = self.BACK
				

""" DO NOT CHANGE THE MAIN SCRIPT BELOW """
		
# Input: number of vertices
# and initialize Graph
N = int(input())
G = Graph(N)
	
# Input: edge_list
edges = input() # format: 1,2 0,1 2,3
edges = edges.split() # : ['1,2', '0,1', '2,3']
	
# Mark edges in G
for e in edges:
	u,v = e.split(",")
	u,v = int(u), int(v)
	G.insert_edge(u,v)

# Run DFS
D = DFS(G)
print('visit_order:', end=" ")
print(D.visit_order)
print('E_label:')

print("    ", end=" ")
for j in range(G.N):
	print('{:4d}'.format(j), end=" ")
print()

i =  0
for rows in D.E_label:
	print("{:4d}".format(i), end=" "); i += 1
	for x in rows:
		if x == D.UNEXPLORED: print("....", end=" ")
		else: print(x, end=" ")
	print()

	
	
	
	
	
