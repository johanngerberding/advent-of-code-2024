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

with open("input.txt", "r") as fp:
    example = [el.strip() for el in fp]

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


result = 0
for letter, area in separated_areas.items():
    for a in area:
        r = fence(a, all_nodes)
        result += r

print(result)
