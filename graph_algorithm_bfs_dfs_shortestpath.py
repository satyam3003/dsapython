"""https://jovian.ai/learn/data-structures-and-algorithms-in-python/lesson/lesson-5-graph-algorithms-bfs-dfs-shortest-paths"""

num_nodes = 5
edges = [(0, 1), (0, 4), (1, 2), (1, 4), (1, 3), (2, 3), (3, 4)]
print(num_nodes, len(edges))


# Adjacency Lists
class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def add_edge(self, edge):
        for n1, n2 in edge:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return "\n".join([f"{n}, {neighbors}" for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()


graph1 = Graph(num_nodes, edges)
print("\nAdjacency Lists")
print(graph1)


# Adjacency matrix
class GraphMatrix:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1][n2] = 1
            self.data[n2][n1] = 1


graph2 = GraphMatrix(num_nodes, edges)
print("\nAdjacency matrix")
print(graph2.data)

# Graph Algorithms
# Breadth first search (BFS)
"""Uses queue: first in first out"""


def bfs(graph, root):
    queue = []  # first in first out
    discovered = [False] * len(graph.data)
    distance = [None] * len(graph.data)  # to get the distance from root node
    parent = [None] * len(graph.data)  # to find the parent node
    discovered[root] = True
    queue.append(root)
    idx = 0
    distance[root] = idx
    while idx < len(queue):
        current = queue[idx]
        idx += 1
        for node in graph.data[current]:
            if not discovered[node]:
                discovered[node] = True
                queue.append(node)
                parent[node] = current
                distance[node] = distance[current] + 1
    return queue, distance, parent


print("\nBFS: Breadth first search")
print(bfs(graph1, 3))


# depth first search DFS
def dfs(graph, root):
    stack = []
    result = []
    discovered = [False] * len(graph.data)
    stack.append(root)
    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            result.append(current)
            for node in graph.data[current]:
                stack.append(node)
    return result


print("\nDFS: Depth first search")
print(dfs(graph1, 3))


# Weighted Graph

class Graph2:
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        if self.weighted:
            self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                n1, n2, weight = edge
                self.data[n1].append(n2)
                self.weight[n1].append(weight)
                if not directed:
                    self.data[n2].append(n1)
                    self.weight[n2].append(weight)
            else:
                n1, n2 = edge
                self.data[n1].append(n2)
                if not directed:
                    self.data[n2].append(n1)


# graph3 = Graph2(num_nodes, edges)
# print(graph3.data)

"""Weighted graph"""
num_nodes2 = 9
edges2 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6),
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

graph4 = Graph2(num_nodes2, edges2, weighted=True)
print("\nWeighted:")
for i in range(len(graph4.data)):
    print(f"{i}: ", end=" ")
    for a in range(len(graph4.data[i])):
        if a < len(graph4.data[i]) - 1:
            print(f"[{graph4.data[i][a]}, {graph4.weight[i][a]}],", end=" ")
        else:
            print(f"[{graph4.data[i][a]}, {graph4.weight[i][a]}]", end="\n")

num_nodes3 = 5
edges3 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
graph5 = Graph2(num_nodes3, edges3, directed=True)
print("\nDirected:")
print(graph5.data)

"""Shortest path algorithm"""


# Dijkstra's algorithm
def shortest_path(graph, source, target):
    queue = []
    parent = [None] * len(graph.data)
    visited = [False] * len(graph.data)
    distance = [float('inf')] * len(graph.data)

    distance[source] = 0
    queue.append(source)
    idx = 0

    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        visited[current] = True
        idx += 1
        update_distances(graph, current, distance)  # update the distance of all the neighbors
        next_node = pick_next_node(distance, visited)  # find the first unvisited node with the smallest distance
        if next_node:
            queue.append(next_node)

    return distance[target]


def update_distances(graph, current, distance, parent=None):
    """Update the distances of the current node's neighbors"""
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current


def pick_next_node(distance, visited):
    """Pick the next univisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node


num_nodes7 = 6
edges7 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]
# num_nodes7, len(edges7)
graph7 = Graph2(num_nodes7, edges7, weighted=True, directed=True)
print(graph7.data)
print(graph7.weight)
print(shortest_path(graph7, 0, 5))
