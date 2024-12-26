example = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


example = [[c for c in line] for line in example.split("\n")]
print(example)

graph = {}

for row in range(len(example)):
    for col in range(len(example[row])):
        if example[row][col] == "#":
            continue
        if example[row][col] == "S":
            start = (row, col)
        if example[row][col] == "E":
            end = (row, col)

        graph[(row, col)] = []
        ...

# dijkstra to find the shortest path
# incorporate the cheat -> how?
# solve dijkstra for cheat maps, remove one tile -> run dijkstra
