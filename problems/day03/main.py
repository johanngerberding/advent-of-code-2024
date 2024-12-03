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

pattern_do = r"do\(\)"
pattern_dont = r"don't\(\)"


def get_matches(pattern, text) -> list[tuple[str, int, int]]:
    return [
        (match.group(), match.start(), match.end())
        for match in re.finditer(pattern, text)
    ]


result = 0
line = "".join(lines)
matches = get_matches(pattern, line)
matches_do = get_matches(pattern_do, line)
matches_dont = get_matches(pattern_dont, line)
matches_do.extend(matches_dont)
matches_enablers = sorted(matches_do, key=lambda x: x[1])
ranges = []
enabled = True
start = 0
print(matches_enablers)
for i in range(len(matches_enablers)):
    if enabled:
        if matches_enablers[i][0] == "do()":
            continue
        if matches_enablers[i][0] == "don't()":
            end = matches_enablers[i][2]
            ranges.append((start, end))
            enabled = False
    else:
        if matches_enablers[i][0] == "don't()":
            continue
        if matches_enablers[i][0] == "do()":
            enabled = True
            start = matches_enablers[i][1]

if enabled:
    ranges.append((start, len(line) - 1))


def check_range(el):
    for ra in ranges:
        if ra[0] <= el[1] and el[2] <= ra[1]:
            return True
    return False


for match in matches:
    if check_range(match):
        parts = match[0].split(",")
        part1 = int(parts[0][4:])
        part2 = int(parts[1][:-1])
        result += part1 * part2

print(f"Part 2: {result}")
