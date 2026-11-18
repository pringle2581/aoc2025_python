from itertools import combinations

def connect(pair):
    c_to = circuits[pair[0]]
    c_from = circuits[pair[1]]
    if c_to != c_from:
        for key, value in circuits.items():
            if value == c_from:
                circuits[key] = c_to

boxes, pairs = [], []
for line in open("./input/8").read().splitlines():
    boxes.append([int(c) for c in line.split(",")])
for c in combinations(range(0, len(boxes)), 2):
    distance = 0
    for i in [0, 1, 2]:
        distance += (boxes[c[0]][i] - boxes[c[1]][i]) ** 2
    pairs.append([c[0], c[1], distance])
circuits = {i:i for i, _ in enumerate(boxes)}
for i, pair in enumerate(sorted(pairs, key=lambda p: p[2])):
    connect(pair)
    if i == 999:
        counts = {}
        for val in circuits.values():
            counts[val] = counts.get(val, 0) + 1
        vals = sorted(counts.values(), reverse=True)
        print("Part 1:", vals[0] * vals[1] * vals[2])
    if len(set(circuits.values())) == 1:
        print("Part 2:", boxes[pair[0]][0] * boxes[pair[1]][0])
        break