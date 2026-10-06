1. Greedy bfs

def greedy_search(graph, current_node, dest, path, q):

    neighbours = graph[current_node][0].keys()

    for n in neighbours:
        if n not in path:
            q[n] = graph[n][1]
            print(f"{n} - {q[n]}")

    while q:
        mn = min(q, key=q.get)

        print(f"Taking min h(n) vertex: {mn}")

        if dest == mn:
            return path + [dest]

        current_node = mn
        del q[mn]

        new_path = greedy_search(
            graph,
            current_node,
            dest,
            path + [current_node],
            q
        )

        if new_path:
            return new_path

    return []


graph = {
    'S': ({'A': 2, 'F': 3}, 6),
    'A': ({'S': 2, 'D': 1}, 3),
    'B': ({'C': 2, 'D': 3}, 2),
    'C': ({'B': 2, 'G': 3}, 2),
    'D': ({'A': 1, 'B': 3, 'G': 2}, 4),
    'F': ({'S': 3, 'G': 2}, 5),
    'G': ({}, 0)
}

source = input("Enter Source Vertex: ")

result = greedy_search(
    graph,
    source,
    'G',
    [source],
    {}
)

print("Remaining path:", result)

2 A*

graph = {
    'A': {'B': 4, 'D': 3},
    'B': {'A': 4, 'C': 2, 'D': 1},
    'C': {'B': 2, 'G': 3},
    'D': {'A': 3, 'B': 1, 'G': 2},
    'G': {}
}

heuristic = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 3,
    'G': 0
}

def a_star(graph, start, goal):
    open_list = [(start, 0)]
    came_from = {}
    g = {start: 0}

    while open_list:
        current = min(
            open_list,
            key=lambda x: x[1] + heuristic[x[0]]
        )

        open_list.remove(current)
        node = current[0]

        print("Taking minimum f(n) vertex:", node)

        if node == goal:
            path = [node]

            while node in came_from:
                node = came_from[node]
                path.append(node)

            path.reverse()
            return path

        for neighbour, cost in graph[node].items():
            new_g = g[current[0]] + cost

            if neighbour not in g or new_g < g[neighbour]:
                g[neighbour] = new_g
                came_from[neighbour] = current[0]

                f = new_g + heuristic[neighbour]

                open_list.append((neighbour, f))

                print(
                    neighbour,
                    "g(n) =", new_g,
                    "h(n) =", heuristic[neighbour],
                    "f(n) =", f
                )

    return []


source = input("Enter Source Vertex: ")
result = a_star(graph, source, 'G')

print("Remaining path:", result)