def accessible(roll):
    result = 0
    for row in [-1, 0, 1]:
        for col in [-1, 0, 1]:
            if (roll[0] + row, roll[1] + col) in rolls:
                result += 1
    return True if result <= 4 else False

part1, part2, rolls = 0, 0, set()
for row, line in enumerate(open("./input/4").read().split()):
    for col, char in enumerate(line):
        if char == "@":
            rolls.add((row, col))
for roll in rolls:
    if accessible(roll):
        part1 += 1
while True:
    removed = 0
    for roll in rolls.copy():
        if accessible(roll):
            rolls.remove(roll)
            removed += 1
    if removed == 0:
        break
    part2 += removed
print("Part 1:", part1, "\nPart 2:", part2)