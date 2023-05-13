class Graph:
    def __init__(self,vertices):
        self.graph = []
        self.V = vertices

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self,parent,i):
        if parent[i] != i:
            parent[i] = self.find(parent,parent[i])
        return parent[i]

    def union(self,rank,parent,x,y):
        if rank[x] < rank[y]:
           parent[x] = y
        elif rank[y] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalAlgo(self):
        i = 0
        e = 0
        result = []
        parent = []
        rank = []
        self.graph = sorted(self.graph,key = lambda item : item[2])
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u , v , w = self.graph[i]
            i += 1
            x = self.find(parent,u)
            y = self.find(parent,v)
            if x != y:
                e += 1
                result.append([u,v,w])
                self.union(rank,parent,x,y)

        minCost = 0
        for u , v, w in result:
            minCost += w
            print(u,v,"--",w)
        print(f"The minimum cost of spanning tree is {minCost}.")

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.KruskalAlgo()