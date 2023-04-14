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

def dfs(graph,root):
    stack = []
    discovered = [False] * len(graph.data)
    result = []
    stack.append(root)
    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            result.append(current)
            for node in graph.data[current]:
               if not discovered[node]:
                  stack.append(node)
    return result

print(dfs(graph1,3))