def getJoltage(bank, battcount):
    joltage = 0
    leftbound = 0
    for currentbatt in range(1, battcount + 1):
        highbatt = leftbound
        for i in range(leftbound + 1, len(bank) - battcount + currentbatt):
            if bank[i] > bank[highbatt]:
                highbatt = i
        leftbound = highbatt + 1
        joltage += bank[highbatt] * 10 ** (battcount - currentbatt)
    return joltage

part1, part2 = 0, 0
for line in open("./input/3").read().splitlines():
    bank = [int(b) for b in line]
    part1 += getJoltage(bank, 2)
    part2 += getJoltage(bank, 12)
print("Part 1:", part1, "\nPart 2:", part2)