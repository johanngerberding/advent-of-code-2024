example = "2333133121414131402"


def transform(disk: str) -> list:
    out = []
    num = 0
    for i, el in enumerate(disk):
        if i % 2 == 0:
            n = num
            num += 1
        else:
            n = -1
        for _ in range(int(el)):
            out.append(n)
    return out


def compress(disk: list) -> list:
    nums = len([el for el in disk if el >= 0])
    compressed = []
    from_back = [el for el in disk[::-1] if el >= 0]
    for i in range(len(disk)):
        if disk[i] >= 0:
            compressed.append(disk[i])
        else:
            compressed.append(from_back.pop(0))
        if len(compressed) == nums:
            break
    return compressed


def checksum(disk: list) -> int:
    checksum = 0
    for i, el in enumerate(disk):
        if el >= 0:
            checksum += i * el
    return checksum


def solve(inp: str) -> int:
    return checksum(compress(transform(inp)))


result = solve(example)
print(result)

with open("input.txt", "r") as fp:
    inp = fp.read().strip()

part1 = solve(inp)
print(f"Part 1: {part1}")
