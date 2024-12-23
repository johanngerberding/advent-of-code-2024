from collections import defaultdict, deque

example = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

# right, down, left, up
# (vertical, horizontal)
orientations = [(0, 1), (-1, 0), (0, -1), (1, 0)]

example = [[el for el in sample] for sample in example.split("\n")]


def init(inp: list) -> tuple:
    start = None
    end = None
    graph = defaultdict(list)
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            if inp[row][col] == "S":
                start = (row, col)
            if inp[row][col] == "E":
                end = (row, col)

            if inp[row][col] in [".", "S", "E"]:
                graph[(row, col)] = []

                for orientation in orientations:
                    adj = (row + orientation[0], col + orientation[1])
                    if (
                        adj[0] < 0
                        or adj[0] >= len(inp)
                        or adj[1] < 0
                        or adj[1] >= len(inp[0])
                    ):
                        continue
                    if inp[adj[0]][adj[1]] in [".", "S", "E"]:
                        graph[(row, col)].append(adj)

    return graph, start, end


def find_all(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return [path]

    paths = []
    for adj in graph[start]:
        if adj not in path:
            new_paths = find_all(graph, adj, end, path)
            paths.extend(new_paths)

    return paths


def calc_score(paths: list[list]):
    scores = []
    for path in paths:
        score = len(path) - 1
        orient = orientations[0]
        for i in range(1, len(path) - 1):
            diff_x = abs(path[i][0] - path[i - 1][0])
            diff_y = abs(path[i][1] - path[i - 1][1])
            next_orient = (diff_x, diff_y)
            if orient == next_orient:
                continue
            else:
                score += 1000
                orient = next_orient
        scores.append(score)
    return scores


graph, start, end = init(example)
print(f"Start: {start}")
print(f"End: {end}")
result = find_all(graph, start, end)
test = min(calc_score(result))
print(f"Example: {test}")

with open("input.txt", "r") as fp:
    data = [[c for c in line.strip()] for line in fp]

graph, start, end = init(data)
print(f"Start: {start}")
print(f"End: {end}")
result = find_all(graph, start, end)
part1 = min(calc_score(result))
print(f"Part 1: {part1}")
