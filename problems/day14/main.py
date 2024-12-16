import math
import re


def solve(inp: list, max_x: int = 101, max_y: int = 103):
    robots = []
    for line in inp:
        px, py, vx, vy = map(int, re.findall(r"-?\d+", line))
        robots.append((px, py, vx, vy))

    for t in range(100):
        for i in range(len(robots)):
            # print(t, robots[i])
            px, py, vx, vy = robots[i]
            npx = px + vx
            if npx >= max_x:
                npx = npx % max_x
            elif npx < 0:
                npx = max_x + npx
            npy = py + vy
            if npy >= max_y:
                npy = npy % max_y
            elif npy < 0:
                npy = max_y + npy
            robots[i] = (npx, npy, vx, vy)
            # break

    quadrants = [0, 0, 0, 0]
    for robot in robots:
        if robot[0] < max_x // 2 and robot[1] < max_y // 2:
            quadrants[0] += 1
        elif robot[0] > max_x // 2 and robot[1] < max_y // 2:
            quadrants[1] += 1
        elif robot[0] < max_x // 2 and robot[1] > max_y // 2:
            quadrants[2] += 1
        elif robot[0] > max_x // 2 and robot[1] > max_y // 2:
            quadrants[3] += 1

    return math.prod(quadrants)


with open("input.txt", "r") as fp:
    lines = fp.read().split("\n")

print(solve(lines))

example = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

example = example.split("\n")

print(solve(example, max_x=11, max_y=7))
