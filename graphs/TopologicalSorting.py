class Graph:
    def __init__(self,numOfNodes,edges,weighted=False,directed=False):
        self.numOfNodes = numOfNodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(numOfNodes)]
        # Jo weights hain wo respective node par hi add hain
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
        print(self.data)

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

numOfNodes = 4
edges = [(1,0),(2,0),(3,0)]
graph = Graph(numOfNodes,edges,directed=True)

def topSort(graph):
    stack = []
    discovered = [False] * len(graph.data)
    for parent in range(len(graph.data)):
        if not discovered[parent]:
            discovered[parent] = True
            for neighbor in graph.data[parent]:
                if not discovered[neighbor]:
                    if neighbor not in stack:
                       stack.append(neighbor)
            if parent not in stack:
                stack.append(parent)

    while len(stack) != 0:
        print(stack.pop(),end = " ")
topSort(graph)