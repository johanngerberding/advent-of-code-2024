def validate_line(line: list) -> bool:
    directions = set()
    for i in range(len(line) - 1):
        diff = line[i + 1] - line[i]
        if abs(diff) > 3 or diff == 0:
            return False
        if diff > 0:
            directions.add(1)
        else:
            directions.add(-1)
        if len(directions) > 1:
            return False
    return True


inp = "input.txt"

with open(inp, "r") as fp:
    data = fp.readlines()

parsed_lines = [line.strip().split(" ") for line in data]
parsed_lines = [[int(el) for el in line] for line in parsed_lines]

val_lines = 0
for line in parsed_lines:
    if validate_line(line):
        val_lines += 1

print(f"Part 1: Safe lines {val_lines}")

val_lines = 0
for line in parsed_lines:
    if validate_line(line):
        val_lines += 1
    else:
        for j in range(len(line)):
            if validate_line([line[k] for k in range(len(line)) if k != j]):
                val_lines += 1
                break

print(f"Part 2: Safe lines {val_lines}")
