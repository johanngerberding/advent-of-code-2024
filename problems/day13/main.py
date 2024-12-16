import re

total = 0

with open("inputs.txt", "r") as fp:
    blocks = fp.read().split("\n\n")

for block in blocks:
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
    px += 10000000000000
    py += 10000000000000
    ca = (px * by - py * bx) / (ax * by - ay * bx)
    cb = (px - ax * ca) / bx
    if ca % 1 == cb % 1 == 0:
        total += 3 * ca + cb

print(total)
