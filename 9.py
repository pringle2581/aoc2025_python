from itertools import combinations

class Point:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

class Ranges:
    def __init__(self, p1, p2):
        self.xmin = min(p1.x, p2.x)
        self.xmax = max(p1.x, p2.x)
        self.ymin = min(p1.y, p2.y)
        self.ymax = max(p1.y, p2.y)

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        x = abs(p1.x - p2.x) + 1
        y = abs(p1.y - p2.y) + 1
        self.area = x * y

def isvalid(rectangle, greens):
    r = Ranges(rectangle.p1, rectangle.p2)
    for g in greens:
        if (r.xmin < g.xmax
        and r.xmax > g.xmin
        and r.ymin < g.ymax
        and r.ymax > g.ymin):
            return False
    return True

reds, greens, rectangles = [], [], []
for line in open("./input/9").read().splitlines():
    reds.append(Point([int(i) for i in line.split(",")]))
for i, red in enumerate(reds):
    greens.append(Ranges(red, reds[i - 1]))
for c in combinations(range(0, len(reds)), 2):
    rectangles.append(Rectangle(reds[c[0]], reds[c[1]]))
rectangles.sort(key=lambda x:x.area, reverse=True)
for rectangle in rectangles:
    if isvalid(rectangle, greens):
        print("Part 1:", rectangles[0].area, "\nPart 2:", rectangle.area)
        break