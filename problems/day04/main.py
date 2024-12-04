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


pattern = r"XMAS"
pattern_back = r"SAMX"

with open("input.txt", "r") as fp:
    rows = fp.readlines()

rows = [row.strip() for row in rows]

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
