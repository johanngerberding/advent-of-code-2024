import re

pattern = r"mul\(\d{1,3},\d{1,3}\)"

with open("input.txt", "r") as fp:
    lines = fp.readlines()

result = 0
for line in lines:
    matches = re.findall(pattern, line)
    for match in matches:
        parts = match.split(",")
        part1 = int(parts[0][4:])
        part2 = int(parts[1][:-1])
        result += part1 * part2

print(f"Part 1: {result}")
