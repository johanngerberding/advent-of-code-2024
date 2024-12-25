import tqdm

example = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

example = example.split("\n\n")

with open("input.txt", "r") as fp:
    data = fp.read()


data = data.split("\n\n")
towels, designs = data
towels = [t.strip() for t in towels.strip().split(",")]

print(f"Number of towels: {len(towels)}")
designs = designs.split("\n")

print(f"Number of designs: {len(designs)}")

# this approach was way too slow
# def splits(string: str):
#     m = len(string) - 1  # number of possible gap positions
#     n = 1 << m  # same as 1 * 2**m
#     res = []

#     for i in range(n):
#         last = 0
#         current = []
#         for j in range(m):
#             if i & (1 << j):
#                 current.append(string[last : j + 1])
#                 last = j + 1

#         current.append(string[last:])
#         res.append(current)

#     return res


cache = {}


def composable(string: str, substrings: list):
    if string == "":
        return True
    if string in cache:
        return cache[string]

    cache[string] = False

    for substr in substrings:
        length = len(substr)
        start = string[:length]
        rest = string[length:]
        if start == substr and composable(rest, substrings):
            cache[string] = True

    return cache[string]


valid = 0
for design in tqdm.tqdm(designs):
    if composable(design, towels):
        valid += 1

    # res = splits(design)
    # for split in res:
    #     if set(split).issubset(set(towels)):
    #         valid += 1
    #         break

print(valid)
