1. hill climbing:

import random

distance = [
    [0, 2, 9, 10],
    [2, 0, 6, 7],
    [9, 6, 0, 3],
    [10, 7, 3, 0]
]

def get_cost(tour):
    cost = 0
    for i in range(len(tour)):
        cost += distance[tour[i-1]][tour[i]]
    return cost


def get_neighbour(tour):
    a, b = random.sample(range(len(tour)), 2)
    tour[a], tour[b] = tour[b], tour[a]
    return tour


def hill_climb():
    current = [0, 1, 2, 3]
    random.shuffle(current)

    current_cost = get_cost(current)

    print("Starting tour:", current, "cost:", current_cost)

    while True:
        neighbour = get_neighbour(current.copy())
        neighbour_cost = get_cost(neighbour)

        print("Current tour:", current)
        print("Neighbour:", neighbour)
        print("Neighbour cost:", neighbour_cost)

        if neighbour_cost < current_cost:
            current = neighbour
            current_cost = neighbour_cost

            print("Current tour:", current)
            print("Current cost:", current_cost)
        else:
            break

    print("Best tour:", current)
    print("Best cost:", current_cost)

    return current, current_cost


hill_climb()

2. alpha beta:

tree = {
    'A': ['B', 'C'],
    'B': [3, 5],
    'C': [6, 9]
}

def minimax_alpha_beta(node, depth, alpha, beta, max_player):

    print("Current node:", node)
    print("Alpha:", alpha)
    print("Beta:", beta)

    if depth == 0 or node not in tree:
        print("Value:", node)
        return node

    if max_player:
        value = float('-inf')

        for child in tree[node]:
            print("Checking child:", child)

            value = max(
                value,
                minimax_alpha_beta(
                    child, depth - 1, alpha, beta, False
                )
            )

            alpha = max(alpha, value)

            print("Current value:", value)
            print("Updated Alpha:", alpha)

            if alpha >= beta:
                print("Pruning branch at node:", node)
                break

        return value

    else:
        value = float('inf')

        for child in tree[node]:
            print("Checking child:", child)

            value = min(
                value,
                minimax_alpha_beta(
                    child, depth - 1, alpha, beta, True
                )
            )

            beta = min(beta, value)

            print("Current value:", value)
            print("Updated Beta:", beta)

            if beta <= alpha:
                print("Pruning branch at node:", node)
                break

        return value


print("Starting Alpha-Beta Search")
print("Starting node: A")

best_score = minimax_alpha_beta(
    'A',
    2,
    float('-inf'),
    float('inf'),
    True
)

print("Best score:", best_score)

