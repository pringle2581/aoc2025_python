part1, part2 = 0, 0
for range_str in open("./input/2").read().split(","):
    range_int = [int(r) for r in range_str.split("-")]
    for i in range(range_int[0], range_int[1] + 1):
        i_str = str(i)
        i_len = len(i_str)
        if i_len % 2 == 0:
            if i_str.startswith(i_str[i_len // 2:]):
                part1 += i
        if (i_str + i_str).index(i_str, 1) != i_len:
            part2 += i
print("Part 1:", part1, "\nPart 2:", part2)