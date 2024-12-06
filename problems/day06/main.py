with open("input.txt", "r") as fp:
    inp = fp.readlines()

inp = [el.strip() for el in inp]

for row in range(len(inp)):
    for col in range(len(inp[row])):
        if inp[row][col] == "^":
            curr = (row, col)

visited = set()
# up, right, down, left
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
curr_dir = 0
visited.add(curr)

while True:
    next_pos = (curr[0] + dirs[curr_dir][0], curr[1] + dirs[curr_dir][1])
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

print(len(visited))
