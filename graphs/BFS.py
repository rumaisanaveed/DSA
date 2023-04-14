class Graph:
    def __init__(self,numOfNodes,edges):
        self.numOfNodes = numOfNodes
        # We have to create a 2d list for each node
        self.data = [[] for _ in range(numOfNodes)]
        #[(1,2) , (1,3)]
        for n1, n2 in edges:
            # 0 1 , 0 4 , 1 2 , 1 3 , 1 4, 2 3, 3 4,
            self.data[n1].append(n2)
            self.data[n2].append(n1)
        #print(self.data)

    def __repr__(self):
        return "\n".join(["{}: {}".format(n, neighbors) for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

numOfNodes = 5
edges = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
graph1 = Graph(numOfNodes,edges)

def bfs(graph,root):
    queue = []
    discovered = [False] * len(graph.data)
    # Because the root is already visited as we started from the root
    discovered[root] = True
    queue.append(root)
    idx = 0
    while idx < len(queue):
        # We are starting from root
        current = queue[idx]
        idx += 1
        # Loop to check for the edges of the current node
        for node in graph.data[current]:
            # If the edges are not discovered yet then, consider them to be discovered
            if not discovered[node]:
                discovered[node] = True
                queue.append(node)
    return queue

print(bfs(graph1,3))