import numpy as np

example = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

A = 3
B = 1

example = [el.split("\n") for el in example.split("\n\n")]
with open("inputs.txt", "r") as fp:
    example = [el.split("\n") for el in fp.read().split("\n\n")]

claws = []
for claw in example:
    button_a = [
        int("".join([c for c in el if c.isnumeric()])) for el in claw[0].split(",")
    ]
    button_b = [
        int("".join([c for c in el if c.isnumeric()])) for el in claw[1].split(",")
    ]
    prize = [
        int("".join([c for c in el if c.isnumeric()])) for el in claw[2].split(",")
    ]
    claws.append((button_a, button_b, prize))


cost = 0
for claw in claws:
    system = [[[claw[0][0], claw[1][0]], [claw[0][1], claw[1][1]]], claw[2]]
    res = np.linalg.solve(system[0], system[1])
    if not int(res[0]) * claw[0][0] + int(res[1]) * claw[1][0] == claw[2][0]:
        continue
    if not int(res[0]) * claw[0][1] + int(res[1]) * claw[1][1] == claw[2][1]:
        continue
    print(f"{system[1]} -> {res}")
    cost += res[0] * A + res[1] * B

print(cost)
