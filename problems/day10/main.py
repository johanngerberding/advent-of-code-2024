example = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

example = example.split("\n")

with open("input.txt", "r") as fp:
    example = [line.strip() for line in fp]

graph: dict[tuple, set[tuple]] = {}

starts = set()
for i in range(len(example)):
    for j in range(len(example[i])):
        node = (i, j, int(example[i][j]))
        adjs = set()
        if i - 1 >= 0:
            adjs.add((i - 1, j, int(example[i - 1][j])))
        if i + 1 <= len(example) - 1:
            adjs.add((i + 1, j, int(example[i + 1][j])))
        if j - 1 >= 0:
            adjs.add((i, j - 1, int(example[i][j - 1])))
        if j + 1 <= len(example[i]) - 1:
            adjs.add((i, j + 1, int(example[i][j + 1])))

        if int(example[i][j]) == 0:
            starts.add(node)
        graph[node] = adjs


def bfs(graph: dict, start: tuple, path=[]):
    path = path + [start]
    if start[2] == 9:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path and node[2] - 1 == start[2]:
            newpaths = bfs(graph, node, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


score = 0
score2 = 0
for start in starts:
    paths = bfs(graph, start)
    score2 += len(paths)
    reachable_nines = set([p[-1] for p in paths])
    score += len(reachable_nines)

print(f"Part 1: {score}")
print(f"Part 2: {score2}")
