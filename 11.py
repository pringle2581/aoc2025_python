def path(start, end):
    if not (start, end) in cache.keys():
        if start == end:
            cache[(start, end)] = 1
        else:
            paths = 0
            for neighbor in graph.get(start, []):
                paths += path(neighbor, end)
            cache[(start, end)] = paths
    return cache[(start, end)]

graph, cache = {}, {}
for line in open("./input/11").read().splitlines():
    split = line.split(": ")
    graph[split[0]] = split[1].split(" ")
fftdac = path("fft", "dac")
dacfft = path("dac", "fft")
if fftdac > dacfft:
    part2 = path("svr", "fft") * fftdac * path("dac", "out")
else:
    part2 = path("svr", "dac") * dacfft * path("fft", "out")
print("Part 1:", path("you", "out"), "\nPart 2:", part2)