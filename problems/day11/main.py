from collections import Counter

example = "125 17"

example = [int(el) for el in example.split(" ")]

with open("input.txt", "r") as fp:
    example = [int(el) for el in fp.read().split(" ")]

samples = Counter(example)

for i in range(75):
    temp = Counter()
    for el, count in samples.items():
        if el == 0:
            temp[1] += count
        elif len(str(el)) % 2 == 0:
            split = len(str(el)) // 2
            nums = [int(str(el)[:split]), int(str(el)[split:])]
            temp[nums[0]] += count
            temp[nums[1]] += count
        else:
            temp[el * 2024] += count
    samples = temp


stones = sum(count for _, count in samples.items())
print(f"Part 2: {stones}")
