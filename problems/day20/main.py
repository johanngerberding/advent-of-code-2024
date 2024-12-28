from copy import deepcopy
from heapq import heapify, heappop, heappush

import tqdm


def print_graph(graph):
    g = ""
    for line in graph:
        g += "".join(line)
        g += "\n"
    print(g)


def get_distances(graph, start):
    distances = {node: float("inf") for node, _ in graph.items()}
    distances[start] = 0

    pq = [(0, start)]
    heapify(pq)

    visited = set()

    while pq:
        current_distance, current_node = heappop(pq)
        if current_node in visited:
            continue

        visited.add(current_node)
        for adj in graph[current_node]:
            dist = current_distance + 1
            if dist < distances[adj]:
                distances[adj] = dist
                heappush(pq, (dist, adj))

    return distances


# example = """###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############"""


# example = [[c for c in line] for line in example.split("\n")]
# print(example)

with open("input.txt", "r") as fp:
    example = [[l for l in line.strip()] for line in fp]

print(example)
graph = {}
optionals = []
graphs = []

print("Lets find optionals")
for row in range(len(example)):
    for col in range(len(example[row])):
        if example[row][col] == "#":
            adjs_opt = []
            if (
                row > 0
                and example[row - 1][col] in [".", "S", "E"]
                and row < len(example) - 1
                and example[row + 1][col] in [".", "S", "E"]
            ):
                adjs_opt.append((row + 1, col))
                adjs_opt.append((row - 1, col))
            if (
                col < len(example[0]) - 1
                and example[row][col + 1] in [".", "S", "E"]
                and col > 0
                and example[row][col - 1] in [".", "S", "E"]
            ):
                adjs_opt.append((row, col - 1))
                adjs_opt.append((row, col + 1))

            if len(adjs_opt) > 0:
                optionals.append((row, col))
print(f"Found {len(optionals)} optionals")

print("Building the original graph...")
org_graph = {}
for row in range(len(example)):
    for col in range(len(example[row])):
        if example[row][col] == "#":
            continue
        if example[row][col] == "S":
            start = (row, col)
            example[row][col] = "."
        if example[row][col] == "E":
            end = (row, col)
            example[row][col] = "."
        adjs = []
        if row > 0 and example[row - 1][col] in [".", "S", "E"]:
            adjs.append((row - 1, col))
        if row < len(example) - 1 and example[row + 1][col] in [".", "S", "E"]:
            adjs.append((row + 1, col))
        if col < len(example[0]) - 1 and example[row][col + 1] in [".", "S", "E"]:
            adjs.append((row, col + 1))
        if col > 0 and example[row][col - 1] in [".", "S", "E"]:
            adjs.append((row, col - 1))

        if len(adjs) > 0:
            org_graph[(row, col)] = adjs

print("Lets create all the optional graphs...")
for opt in tqdm.tqdm(optionals):
    graph = {}
    nexample = deepcopy(example)
    nexample[opt[0]][opt[1]] = "."
    for row in range(len(nexample)):
        for col in range(len(nexample[row])):
            if nexample[row][col] == "#":
                continue
            adjs = []
            if row > 0 and nexample[row - 1][col] == ".":
                adjs.append((row - 1, col))
            if row < len(nexample) - 1 and nexample[row + 1][col] == ".":
                adjs.append((row + 1, col))
            if col < len(nexample[0]) - 1 and nexample[row][col + 1] == ".":
                adjs.append((row, col + 1))
            if col > 0 and nexample[row][col - 1] == ".":
                adjs.append((row, col - 1))

            if len(adjs) > 0:
                graph[(row, col)] = adjs

    graphs.append(graph)

print(f"Start calculating distances...")
org_distance = get_distances(org_graph, start)[end]
print(f"original distance: {org_distance}")
result = 0
for graph in graphs:
    distance = get_distances(graph, start)[end]
    print(f"cheat distance: {distance} | saved {org_distance - distance}")
    if org_distance - distance >= 100:
        result += 1

print(f"Part 1: {result}")
# dijkstra to find the shortest path
# incorporate the cheat -> how?
# solve dijkstra for cheat maps, remove one tile -> run dijkstra
