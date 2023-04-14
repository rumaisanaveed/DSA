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

def shortestPaths(graph,source,target):
    visited = [False] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    queue = []
    distance[source] = 0
    queue.append(source)
    idx = 0
    while idx < len(queue) and not visited[target]:
        # current = 0
        current = queue[idx]
        # As we have visited the node therefore, we have set it to True
        visited[current] = True
        idx += 1
        # update the distances of all the neighbors
        update_distances(graph,current,distance)
        # Pick the next node with the smallest distance
        next_node = pick_next_node(distance,visited)
        if not next_node:
            queue.append(next_node)
    # We are returning distance[target] because the list contains the shortest distance from source to all nodes
    return distance[target]

def update_distances(graph, current, distance):
    """Update the distances of the current node's neighbors"""
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i] # 3
        # Distance of a node is the sum of current node and weight
        # For shortest distance
        '''Important'''
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight

def pick_next_node(distance, visited):
    """Pick the next univisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node

numOfNodes2 = 9
edges2 = [(0,1,3),(0,3,2),(0,8,4),(1,7,4),(2,7,2),(2,3,6),(2,5,1),(3,4,1),(4,8,8),(5,6,8)]
graph2 = Graph(numOfNodes2,edges2,weighted = True)
print(shortestPaths(graph2,0,2))