'''Prim's Algorithm to find the minimum spanning tree'''

# 1) Pick the first vertex as starting vertex
# 2) Now, select the vertex with the minimum weight
# 3) Put the selected vertex in mst
# 4) Now, check for every adjacent vertex of the current vertex and update their distances and
# also update their parents
# 5) Do it for every vertex in the graph and return the mst set

class PrimsAlgo:
    def __init__(self,noOfVer):
        self.noOfVer = noOfVer
        self.graph = [0 for i in range(noOfVer)
                      for j in range(noOfVer)]

    def printMst(self,parent):
        print("Edge\tWeight")
        for i in range(1,self.noOfVer):
            print(parent[i],"-",i,"\t",self.graph[i][parent[i]])

    def pickNextNode(self,distances,mst):
        minNode = None
        minDist = float('inf')
        for node in range(self.noOfVer):
            if minDist > distances[node] and not mst[node]:
                minNode = node
                minDist = distances[node]
        return minNode

    def primAlgo(self):
        # As up till now no vertex is part of mst
        mst = [False] * self.noOfVer
        # Assign tentative distances to all the vertices or nodes
        mstWeight = [float('inf')] * self.noOfVer
        # As we know the weight of node 1 is zero
        mstWeight[0] = 0
        # parent list to store the parents of all the vertices
        parent = [None] * self.noOfVer
        # Because the starting node has no parent
        parent[0] = -1
        # We have to traverse the whole graph
        for vertex in range(self.noOfVer):
            # Pick the vertex with minimum weight
            u = self.pickNextNode(mstWeight, mst)
            # Include it in mst
            mst[u] = True
            # Now, update the weights or distances of all the vertices adjacent to the vertex u
            for v in range(self.noOfVer):
                if self.graph[u][v] < mstWeight[v] and self.graph[u][v] > 0 and not mst[v]:
                    mstWeight[v] = self.graph[u][v]
                    parent[v] = u
        self.printMst(parent)

g = PrimsAlgo(9)
g.graph = [[0,4,0,0,0,0,0,8,0],
           [4,0,8,0,0,0,0,11,0],
           [0,8,0,7,0,4,0,0,2],
           [0,0,7,0,9,14,0,0,0],
           [0,0,0,9,0,10,0,0,0],
           [0,0,4,14,10,0,2,0,0],
           [0,0,0,0,0,2,0,1,6],
           [8,11,0,0,0,0,1,0,7],
           [0,0,2,0,0,0,6,7,0]]
print(g.primAlgo())