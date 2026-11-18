part1, part2, unsorted, fresh, available = 0, 0, [], [], []
for line in open("./input/5").read().splitlines():
    if "-" in line:
        unsorted.append([int(r) for r in line.split("-")])
    elif line:
        available.append(int(line))
for f in sorted(unsorted):
    if not fresh or fresh[-1][1] < f[0]:
        fresh.append(f)
    else:
        fresh[-1] = (fresh[-1][0], max(fresh[-1][1], f[1]))
for a in available:
    for f in fresh:
        if a >= f[0] and a <= f[1]:
            part1 += 1
            break
for f in fresh:
    part2 += f[1] - f[0] + 1
print("Part 1:", part1, "\nPart 2:", part2)