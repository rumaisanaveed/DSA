class Graph:
    def __init__(self,numOfNodes,edges):
        self.numOfNodes = numOfNodes
        self.data = []
        for _ in range(numOfNodes):
            r = []
            for _ in range(numOfNodes):
                r.append(0)
            self.data.append(r)
        for n1, n2 in edges:
            self.data[n1][n2] = 1
            self.data[n2][n1] = 1

    def displayGraph(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                print(self.data[i][j],end = "\t")
            print()
numOfNodes = 5
edges = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
g = Graph(numOfNodes,edges)
g.displayGraph()