1 miss and cann :

from collections import deque

moves = [(2,0),(0,2),(1,1),(1,0),(0,1)]

def valid(ml, cl, mr, cr):
    if ml < 0 or cl < 0 or mr < 0 or cr < 0:
        return False
    if ml > 0 and ml < cl:
        return False
    if mr > 0 and mr < cr:
        return False
    return True

def solve():
    start = (3,3,1)
    goal = (0,0,0)
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        if state in visited:
            continue
        visited.add(state)

        ml, cl, boat = state

        for m, c in moves:
            if boat == 1:
                nml, ncl, nb = ml-m, cl-c, 0
            else:
                nml, ncl, nb = ml+m, cl+c, 1

            nmr, ncr = 3-nml, 3-ncl

            if valid(nml,ncl,nmr,ncr):
                new = (nml,ncl,nb)
                queue.append((new, path+[new]))

steps = solve()

if steps:
    for i, (m,c,b) in enumerate(steps):
        side = "left" if b == 1 else "right"
        print(f"Step {i}: Missionaries={m}, Cannibals={c}, Boat={side}")
else:
    print("No solution found")

2. Number Puzzle:

from collections import deque

goal = "123456780"

moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def bfs(start):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        if state in visited:
            continue
        visited.add(state)

        zero = state.index('0')

        for move in moves[zero]:
            new_state = list(state)
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            new_state = ''.join(new_state)

            queue.append((new_state, path + [new_state]))

    return None


start = "123456780"
solution = bfs(start)

if solution:
    print("Steps to solve:")
    for s in solution:
        print(s[:3])
        print(s[3:6])
        print(s[6:9])
        print()
else:
    print("No solution found")