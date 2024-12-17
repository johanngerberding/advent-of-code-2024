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

example = example.split("\n\n")
canvas = example[0].strip().split("\n")
canvas = [[c for c in el] for el in canvas]
moves = "".join(example[1].split("\n"))

print(canvas)
print(moves)

for row in range(len(canvas)):
    for col in range(len(canvas[row])):
        if canvas[row][col] == "@":
            robot = (row, col)
            canvas[row][col] = "."


for move in moves:
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
            next_symbols = canvas[robot[0]][robot[1] :]
            print(next_symbols)
        ...
    elif move == "<":
        left = canvas[robot[0]][robot[1] - 1]
        if left == "#":
            continue
        elif left == ".":
            robot = (robot[0], robot[1] - 1)
        elif left == "O":
            ...
        ...
    elif move == "^":
        up = canvas[robot[0] - 1][robot[1]]
        if up == "#":
            continue
        elif up == ".":
            robot = (robot[0] - 1, robot[1])
        elif up == "O":
            ...
        ...
    elif move == "v":
        down = canvas[robot[0] + 1][robot[1]]
        if down == "#":
            continue
        elif down == ".":
            robot = (robot[0] + 1, robot[1])
        elif down == "O":
            ...
        ...
    else:
        raise ValueError(f"Illegal move: {move}")
