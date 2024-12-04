import re


def generate_cols(rows: list) -> list:
    cols = []
    for col in range(len(rows[0])):
        c = ""
        for row in rows:
            c += row[col]
        cols.append(c)
    return cols


def generate_diags(rows: list) -> list:
    diagonals = []
    # i need the indexes of all diagonals for row x cols
    for row in range(len(rows)):
        col = 0
        val = ""
        while True:
            val += rows[row][col]
            row += 1
            col += 1
            if row >= len(rows) or row < 0:
                break
            if col >= len(rows[0]) or col < 0:
                break
        diagonals.append(val)

    for col in range(1, len(rows[0])):
        row = 0
        val = ""
        while True:
            val += rows[row][col]
            row += 1
            col += 1
            if row >= len(rows) or row < 0:
                break
            if col >= len(rows[0]) or col < 0:
                break
        diagonals.append(val)

    for row in range(len(rows)):
        col = len(rows[0]) - 1
        val = ""
        while True:
            val += rows[row][col]
            row += 1
            col -= 1
            if row >= len(rows) or row < 0:
                break
            if col >= len(rows[0]) or col < 0:
                break
        diagonals.append(val)

    for col in range(len(rows[0]) - 2, 0, -1):
        row = 0
        val = ""
        while True:
            val += rows[row][col]
            row += 1
            col -= 1
            if row >= len(rows) or row < 0:
                break
            if col >= len(rows[0]) or col < 0:
                break
        diagonals.append(val)

    return diagonals


def find(rows: list, part: str):
    cols = generate_cols(rows)
    diags = generate_diags(rows)
    rows.extend(cols)
    rows.extend(diags)

    result = 0
    for line in rows:
        matches = re.findall(pattern, line)
        result += len(matches)
        matches_back = re.findall(pattern_back, line)
        result += len(matches_back)

    print(f"{part}: {result}")


def check(row: int, col: int, rows: list) -> bool:
    """Check if neighbors form XMAS"""
    if row > 0 and col > 0 and row < (len(rows) - 1) and col < (len(rows[0]) - 1):
        neighbors = (
            rows[row - 1][col - 1]
            + rows[row - 1][col + 1]
            + rows[row + 1][col - 1]
            + rows[row + 1][col + 1]
        )
        if (
            neighbors == "MSMS"
            or neighbors == "MMSS"
            or neighbors == "SMSM"
            or neighbors == "SSMM"
        ):
            return True
    return False


pattern = r"XMAS"
pattern_back = r"SAMX"

with open("input.txt", "r") as fp:
    rows = fp.readlines()

rows = [row.strip() for row in rows]
rows_part2 = [row.strip() for row in rows]

test = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

test = test.split()

find(test, "Test")
find(rows, "Part 1")

part2 = 0
for row in range(len(rows_part2)):
    for col in range(len(rows_part2[row])):
        if rows_part2[row][col] == "A":
            if check(row, col, rows_part2):
                part2 += 1

print(f"Part 2: {part2}")
