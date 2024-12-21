from copy import deepcopy

example = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

with open("input.txt", "r") as fp:
    data = fp.read()

data = data.split("\n\n")
canvas = data[0].strip().split("\n")
canvas = [[c for c in el] for el in canvas]
moves = "".join(data[1].split("\n"))


# example = example.split("\n\n")
# canvas = example[0].strip().split("\n")
# canvas = [[c for c in el] for el in canvas]
# moves = "".join(example[1].split("\n"))


def print_canvas(canvas: list, robot: tuple):
    can = deepcopy(canvas)
    can[robot[0]][robot[1]] = "@"
    for line in can:
        print("".join(line))
    print("")


def gps(canvas: list) -> int:
    result = 0
    for i in range(len(canvas)):
        for j in range(len(canvas[i])):
            if canvas[i][j] == "O":
                result += i * 100 + j
    return result


for row in range(len(canvas)):
    for col in range(len(canvas[row])):
        if canvas[row][col] == "@":
            robot = (row, col)
            canvas[row][col] = "."


print_canvas(canvas, robot)

for move in moves:
    print(f"Move: {move}")
    if move == ">":
        right = canvas[robot[0]][robot[1] + 1]
        if right == "#":
            continue
        elif right == ".":
            robot = (robot[0], robot[1] + 1)
        elif right == "O":
            # look forward and check if we can push
            # find next # or .
            # if # is before . than robot stays in position
            # if . comes before, shift stuff
            next_symbols = canvas[robot[0]][robot[1] + 2 :]
            if "." not in next_symbols:
                # cannot move
                continue
            else:
                # there is room to move stuff
                # find next .
                end = next_symbols.index("#")
                next_pos = next_symbols.index(".")
                if end < next_pos:
                    # cannot move
                    continue
                # shift
                assert canvas[robot[0]][robot[1] + 2 + next_pos] == "."
                canvas[robot[0]][robot[1] + 2 + next_pos] = "O"
                canvas[robot[0]][robot[1] + 1] = "."
                robot = (robot[0], robot[1] + 1)
    elif move == "<":
        left = canvas[robot[0]][robot[1] - 1]
        if left == "#":
            continue
        elif left == ".":
            robot = (robot[0], robot[1] - 1)
        elif left == "O":
            # look forward and check if we can push
            # find next # or .
            # if # is before . than robot stays in position
            # if . comes before, shift stuff
            next_symbols = canvas[robot[0]][: robot[1] - 1]
            if "." not in next_symbols:
                # cannot move
                continue
            else:
                # there is room to move stuff
                # find next .
                end = next_symbols[::-1].index("#")
                next_pos = next_symbols[::-1].index(".")
                if end < next_pos:
                    # cannot move
                    continue
                # shift
                # end_idx = len(next_symbols) - 1 - end
                # next_pos_idx = len(next_symbols) - 1 - next_pos
                assert canvas[robot[0]][robot[1] - 2 - next_pos] == "."
                canvas[robot[0]][robot[1] - 2 - next_pos] = "O"
                canvas[robot[0]][robot[1] - 1] = "."
                robot = (robot[0], robot[1] - 1)
    elif move == "^":
        up = canvas[robot[0] - 1][robot[1]]
        if up == "#":
            continue
        elif up == ".":
            robot = (robot[0] - 1, robot[1])
        elif up == "O":
            next_symbols = [canvas[row][robot[1]] for row in range(robot[0] - 1)]
            if "." not in next_symbols:
                # cannot move
                continue
            else:
                # there is room to move stuff
                # find next .
                end = next_symbols[::-1].index("#")
                next_pos = next_symbols[::-1].index(".")
                if end < next_pos:
                    # cannot move
                    continue
                # shift
                # end_idx = len(next_symbols) - 1 - end
                # next_pos_idx = len(next_symbols) - 1 - next_pos
                assert canvas[robot[0] - 2 - next_pos][robot[1]] == "."
                canvas[robot[0] - 2 - next_pos][robot[1]] = "O"
                canvas[robot[0] - 1][robot[1]] = "."
                robot = (robot[0] - 1, robot[1])
    elif move == "v":
        down = canvas[robot[0] + 1][robot[1]]
        if down == "#":
            continue
        elif down == ".":
            robot = (robot[0] + 1, robot[1])
        elif down == "O":
            next_symbols = [
                canvas[row][robot[1]] for row in range(robot[0] + 2, len(canvas))
            ]
            if "." not in next_symbols:
                # cannot move
                continue
            else:
                # there is room to move stuff
                # find next .
                end = next_symbols.index("#")
                next_pos = next_symbols.index(".")
                if end < next_pos:
                    # cannot move
                    continue
                # shift
                assert canvas[robot[0] + 2 + next_pos][robot[1]] == "."
                canvas[robot[0] + 2 + next_pos][robot[1]] = "O"
                canvas[robot[0] + 1][robot[1]] = "."
                robot = (robot[0] + 1, robot[1])
    else:
        raise ValueError(f"Illegal move: {move}")

    print_canvas(canvas, robot)


result = gps(canvas)

print(result)
