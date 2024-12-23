import heapq

# the heapq automatically sorts by the first value, here the cost

grid = [list(line.strip()) for line in open("input.txt", "r")]

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            sr = r
            sc = c
            break
    else:
        continue
    break

pq = [(0, sr, sc, 0, 1)]
seen = {(sr, sc, 0, 1)}

while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)
    seen.add((r, c, dr, dc))
    if grid[r][c] == "E":
        print(f"Part 1: {cost}")
        break
    # three cases, go in same direction, turn 90 degrees
    for new_cost, nr, nc, ndr, ndc in [
        (cost + 1, r + dr, c + dc, dr, dc),
        (cost + 1000, r, c, dc, -dr),
        (cost + 1000, r, c, -dc, dr),
    ]:
        if grid[nr][nc] == "#":
            continue  # hit the wall
        if (nr, nc, ndr, ndc) in seen:
            continue
        heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))
