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


# empty space can also be a file with value -1
class File:
    def __init__(self, position: int, size: int, value: int):
        self.position = position
        self.size = size
        self.value = value
        self.fixed = False

    def __repr__(self) -> str:
        return self.size * f"{self.value}"

    def checksum(self):
        return sum(
            [i * self.value for i in range(self.position, self.position + self.size)]
        )


def parse(disk: str) -> list[File]:
    parsed = []
    num = 0
    pos = 0
    for i, el in enumerate(disk):
        if i % 2 == 0:
            parsed.append(File(pos, int(el), num))
            num += 1
            pos += int(el)
        else:
            pos += int(el)

    return parsed


result = solve(example)
print(result)


def solve2(inp: str):
    parsed_files = parse(inp)
    curr = len(parsed_files) - 1
    for _ in range(len(parsed_files)):
        last = parsed_files[curr]
        if last.fixed:
            curr -= 1
            continue
        found = False
        for i in range(curr - 1):
            diff = parsed_files[i + 1].position - (
                parsed_files[i].position + parsed_files[i].size
            )
            if diff >= last.size:
                last.position = parsed_files[i].position + parsed_files[i].size
                parsed_files.insert(i + 1, last)
                # remove element from old position
                parsed_files.pop(curr + 1)
                found = True
                break
        if not found:
            curr -= 1
        last.fixed = True

    checksums = 0
    for parsed_file in parsed_files:
        checksums += parsed_file.checksum()

    return checksums


print(solve2(example))

with open("input.txt", "r") as fp:
    inp = fp.read().strip()

part1 = solve(inp)
print(f"Part 1: {part1}")

part2 = solve2(inp)
print(f"Part 2: {part2}")
