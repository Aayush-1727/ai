# AI Practical 8

import itertools

variables = ["A", "B", "C"]
colors = ["red", "blue", "yellow"]

all_assignments = itertools.product(colors, repeat=len(variables))

def valid(i):
    A, B, C = i
    return (A != B) and (B != C) and (A != C)

solutions = []

for i in all_assignments:
    if valid(i):
        solutions.append(dict(zip(variables, i)))

print("Valid colourings of the map:")
for sol in solutions:
    print(sol)