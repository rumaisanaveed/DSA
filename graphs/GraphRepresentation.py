class Graph:
    def __init__(self,numOfNodes,edges,weighted=False,directed=False):
        self.numOfNodes = numOfNodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(numOfNodes)]
        self.weight = [[] for _ in range(numOfNodes)]
        for edge in edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            # both for directed and undirected
            else:
                # work without weights
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)

    def displayGraph(self):
        if self.weighted:
            for i in range(len(self.data)):
                temp = []
                for j in range(len(self.data[i])):
                    temp.append((self.data[i][j],self.weight[i][j]))
                print(i,":",temp)
        else:
            for i in range(len(self.data)):
                print(i, ":", self.data[i])

numOfNodes = 5
edges = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
graph1 = Graph(numOfNodes,edges)
graph1.displayGraph()
