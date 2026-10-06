1. DFS

def dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()

dfs(graph, 'A', visited)

2. BFS

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node)
            visited.add(node)

            for neighbour in graph[node]:
                queue.append(neighbour)


def all_paths(start, end, graph):
    todo = [[start]]

    while todo:
        path = todo.pop()

        for next_node in graph[path[-1]]:
            if next_node in path:
                continue

            if next_node == end:
                yield path + [next_node]
            else:
                todo.append(path + [next_node])


def bfs_shortest_path(graph, source, destination):
    queue = deque([[source]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == destination:
            return path

        for neighbour in graph[node]:
            if neighbour not in path:
                new_path = path + [neighbour]
                queue.append(new_path)

    return None


graph = {
    'A': ['B', 'D'],
    'B': ['C', 'F'],
    'C': ['E', 'G', 'H'],
    'G': ['E', 'H'],
    'E': ['B', 'F'],
    'F': ['A'],
    'D': ['F'],
    'H': ['A']
}

print("Graph Traversal:")
bfs(graph, 'A')

print("All paths are:")
for p in all_paths('A', 'E', graph):
    print(p)

print("Shortest path of graph is:")
print(bfs_shortest_path(graph, 'A', 'E'))