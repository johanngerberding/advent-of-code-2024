# with open("input.txt", "r") as fp:
#     inp = fp.readlines()

# inp = [el.strip() for el in inp]

inp = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
inp = inp.split()

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
curr_dir = 0

for row in range(len(inp)):
    for col in range(len(inp[row])):
        if inp[row][col] == "^":
            curr = (row, col, curr_dir)
            curr_pos = (row, col)

visited_with_direction = set()
visited = set()
# up, right, down, left
visited.add(curr_pos)
visited_with_direction.add(curr)

# i think we have a circle if the next pos is in visited with the same direction
# for every position you are in, you have to check where the right position of you
# was already visited and if it has the same direction as if there was an obstacle in
# front of you
obstruction_positions = 0

while True:
    next_pos = (curr[0] + dirs[curr_dir][0], curr[1] + dirs[curr_dir][1])
    right_dir = curr_dir + 1
    if right_dir > 3:
        right_dir = 0
    right_pos_with_dir = (
        curr[0] + dirs[right_dir][0],
        curr[1] + dirs[right_dir][1],
        right_dir,
    )

    if right_pos_with_dir in visited_with_direction:
        obstruction_positions += 1

    if (
        next_pos[0] < 0
        or next_pos[0] >= len(inp)
        or next_pos[1] < 0
        or next_pos[1] >= len(inp[0])
    ):
        # we are done
        break
    while inp[next_pos[0]][next_pos[1]] == "#":
        # switch direction
        curr_dir += 1
        if curr_dir > 3:
            curr_dir = 0

        next_pos = (curr[0] + dirs[curr_dir][0], curr[1] + dirs[curr_dir][1])
    # set new position
    curr = next_pos
    visited.add(curr)
    visited_with_direction.add((curr[0], curr[1], curr_dir))
    print(visited)

print(obstruction_positions)
