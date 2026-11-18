part1, part2, dial = 0, 0, 50
for line in open("./input/1").read().split():
    direction = -1 if line.startswith("L") else 1
    for _ in range(int(line[1:])):
        dial = (dial + direction) % 100
        if dial == 0:
            part2 += 1
    if dial == 0:
        part1 += 1
print("Part 1:", part1, "\nPart 2:", part2)