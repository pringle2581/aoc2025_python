def calc(numbers, symbol):
    if symbol == "+":
        result = 0
        for n in numbers:
            result += int(n)
    elif symbol == "*":
        result = 1
        for n in numbers:
            result *= int(n)
    return result

part1, part2 = 0, 0
ws = open("./input/6").read().splitlines()
rows = len(ws) - 1
cols = len(ws[0])
numbers = [""] * rows
numbers2 = []
for col in range(0, cols):
    nums = [""] * rows
    num2 = ""
    if not ws[rows][col].isspace():
        symbol = ws[rows][col]
    for row in range(0, rows):
        num2 += ws[row][col]
        if not ws[row][col].isspace():
            nums[row] += ws[row][col]
    if len(set(nums)) > 1 or len(nums[0]) > 0:
        for i in range(0, rows):
            numbers[i] += nums[i]
    if len(set(nums)) == 1 and len(nums[0]) == 0 or col == cols - 1:
        part1 += calc(numbers, symbol)
        numbers = [""] * rows
    if not num2.isspace():
        numbers2.append(num2.strip())
    if num2.isspace() or col == cols - 1:
        part2 += calc(numbers2, symbol)
        numbers2 = []
print("Part 1:", part1, "\nPart 2:", part2)