import itertools

import tqdm


def evaluate(numbers: list, ops: list, target: int):
    """Eval from left to right without precedence rules"""
    result = numbers[0]
    if result > target:
        return False

    for i, op in enumerate(ops[:-1]):
        if op == "&":
            result = int(str(result) + str(numbers[i + 1]))
        elif op == "+":
            result += numbers[i + 1]
        else:
            result *= numbers[i + 1]

        if result > target:
            return False

    return result == target


with open("input.txt", "r") as fp:
    inp = fp.readlines()

inp = [el.strip() for el in inp]
inp = [el.split(":") for el in inp]

# example = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""

# example = example.split("\n")
# inp = [el.split(":") for el in example]

ops_cache = {}
calibration_result = 0
for sample in tqdm.tqdm(inp):
    assert len(sample) == 2
    result = int(sample[0])
    numbers = [int(el) for el in sample[1].split(" ") if el]

    num_ops = len(numbers) - 1
    if num_ops not in ops_cache:
        ops_cache[num_ops] = list(itertools.product("*+&", repeat=num_ops))

    for op in ops_cache[num_ops]:
        _ops = list(op)
        _ops.append("")
        if evaluate(numbers, _ops, result):
            calibration_result += result
            break


print(calibration_result)
