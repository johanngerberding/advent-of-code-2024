import tqdm

data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

data = data.split("\n\n")

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


def composabel_count(substrings: list, string: str):
    n = len(string)
    dp = [0] * (n + 1)
    dp[0] = 0

    for i in range(n):
        if dp[i] == 0:
            continue
        for substr in substrings:
            if string[i:].startswith(substr):
                dp[i + len(substr)] += dp[i]

    return dp[n]


def count_ways_to_build(word_list, target):
    memo = {}

    def helper(pos):
        # Base cases
        if pos == len(target):
            return 1
        if pos > len(target):
            return 0
        if pos in memo:
            return memo[pos]

        ways = 0
        # Try each word from current position
        for word in word_list:
            if target[pos:].startswith(word):
                ways += helper(pos + len(word))

        memo[pos] = ways
        return ways

    return helper(0)


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


result = 0
for design in tqdm.tqdm(designs):
    # if composable(design, towels):
    #     valid += 1
    ways = count_ways_to_build(towels, design)
    result += ways

print(result)
