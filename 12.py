part1 = 0
for line in open("./input/12").read().splitlines():
    if "x" in line:
        split = line.split(": ")
        size = [int(i) for i in split[0].split("x")]
        gift = [int(i) for i in split[1].split(" ")]
        if size[0] * size[1] >= sum(gift) * 9:
            part1 += 1
print("Part 1:", part1, "\nPart 2: ♥ all done! ♥")