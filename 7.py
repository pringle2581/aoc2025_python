lines = open("./input/7").read().splitlines()
beams = {}
beams[lines[0].index("S")] = 1
splits = 0
for line in lines:
    for i, char in enumerate(line):
        if char == "^" and beams[i] > 0:
            for n in [-1, 1]:
                beams[i + n] = beams.get(i + n, 0) + beams[i]
            beams[i] = 0
            splits += 1
print("Part 1:", splits, "\nPart 2:", sum(beams.values()))