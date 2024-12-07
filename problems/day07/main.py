import itertools

import tqdm


def evaluate(numbers: list, ops: list, target: int) -> bool:
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


def main():
    with open("input.txt", "r") as fp:
        inp = [line.strip().split(":") for line in fp]

    for o, p in zip(["*+", "*+&"], ["Part 1:", "Part 2:"]):
        ops_cache = {}
        calibration_result = 0
        for sample in tqdm.tqdm(inp):
            assert len(sample) == 2
            result = int(sample[0])
            numbers = [int(el) for el in sample[1].split(" ") if el]

            num_ops = len(numbers) - 1
            if num_ops not in ops_cache:
                ops_cache[num_ops] = list(itertools.product(o, repeat=num_ops))

            for op in ops_cache[num_ops]:
                _ops = list(op)
                _ops.append("")
                if evaluate(numbers, _ops, result):
                    calibration_result += result
                    break

        print(f"{p} {calibration_result}")


if __name__ == "__main__":
    main()
