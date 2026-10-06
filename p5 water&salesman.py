1. waterjug

from collections import deque

def water_jug_bfs():
    max_a, max_b = 5, 4
    visited = set()
    queue = deque()

    queue.append((0, 0))

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        print(f"Jug A: {a}L, Jug B: {b}L")

        if a == 2 or b == 2:
            print("Found a solution")
            return

        states = [
            (max_a, b),  # Fill A
            (a, max_b),  # Fill B
            (0, b),      # Empty A
            (a, 0),      # Empty B
            (min(a + b, max_a), b - min(a + b, max_a)),
            (a - min(a + b, max_b), min(a + b, max_b))
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("No solution found")

water_jug_bfs()

2. salesperson

from itertools import permutations

dist = [
    [0, 10, 15, 20],
    [10, 30, 35, 25],
    [15, 25, 0, 30],
    [20, 25, 30, 0]
]

n = len(dist)
cities = range(1, n)

min_distance = float('inf')
best_path = None

for path in permutations(cities):
    current_path = (0,) + path + (0,)
    distance = 0

    for i in range(len(current_path) - 1):
        distance += dist[current_path[i]][current_path[i + 1]]

    if distance < min_distance:
        min_distance = distance
        best_path = current_path

print("Shortest distance:", min_distance)
print("Best path:", best_path)