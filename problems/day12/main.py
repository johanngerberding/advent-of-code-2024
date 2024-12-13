example = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


example = example.split("\n")

# with open("input.txt", "r") as fp:
#     example = [el.strip() for el in fp]

areas = {}

for i in range(len(example)):
    for j in range(len(example[i])):
        if example[i][j] in areas:
            areas[example[i][j]].add((i, j))
        else:
            areas[example[i][j]] = set([(i, j)])

all_nodes = set()
for _, val in areas.items():
    all_nodes.update(val)


def get_neighbors(curr: tuple, nodes: set) -> set:
    neighbors = set()
    up = (curr[0] - 1, curr[1])
    if up in nodes:
        neighbors.add(up)
    down = (curr[0] + 1, curr[1])
    if down in nodes:
        neighbors.add(down)
    left = (curr[0], curr[1] - 1)
    if left in nodes:
        neighbors.add(left)
    right = (curr[0], curr[1] + 1)
    if right in nodes:
        neighbors.add(right)
    return neighbors


separated_areas = {}
for letter, nodes in areas.items():
    sep_areas = []
    while len(nodes) > 0:
        curr = nodes.pop()
        area = set([curr])
        neighbors = get_neighbors(curr, nodes)
        while len(neighbors) > 0:
            curr = neighbors.pop()
            nodes.remove(curr)
            area.add(curr)
            neighbors.update(get_neighbors(curr, nodes))
        sep_areas.append(area)
    separated_areas[letter] = sep_areas


def fence(area: set, nodes: set) -> int:
    fence = 0
    for node in area:
        per_node_fence = 0
        neighbors = [
            (node[0] - 1, node[1]),
            (node[0] + 1, node[1]),
            (node[0], node[1] - 1),
            (node[0], node[1] + 1),
        ]
        for neighbor in neighbors:
            if neighbor not in nodes:
                per_node_fence += 1
            elif neighbor not in area:
                per_node_fence += 1
        fence += per_node_fence
    return fence * len(area)


def sides(area: set) -> int:
    sides = 0
    # get all left elements
    lefts = {}
    for node in area:
        if node[0] in lefts:
            if node[1] < lefts[node[0]]:
                lefts[node[0]] = node[1]
        else:
            lefts[node[0]] = node[1]

    sides += len(set(v for _, v in lefts.items()))

    rights = {}
    for node in area:
        if node[0] in rights:
            if node[1] > rights[node[0]]:
                rights[node[0]] = node[1]
        else:
            rights[node[0]] = node[1]

    sides += len(set(v for _, v in rights.items()))

    ups = {}
    for node in area:
        if node[1] in ups:
            if node[0] < ups[node[1]]:
                ups[node[1]] = node[0]
        else:
            ups[node[1]] = node[0]

    sides += len(set(v for _, v in ups.items()))

    downs = {}
    for node in area:
        if node[1] in downs:
            if node[0] > downs[node[1]]:
                downs[node[1]] = node[0]
        else:
            downs[node[1]] = node[0]

    sides += len(set(v for _, v in downs.items()))

    return sides * len(area)


part1 = 0
part2 = 0
for letter, area in separated_areas.items():
    print(f"------ {letter} ------")
    for a in area:
        r = fence(a, all_nodes)
        part1 += r
        s = sides(a)
        print(letter, s)
        part2 += s


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
