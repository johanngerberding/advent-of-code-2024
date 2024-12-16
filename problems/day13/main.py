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
print(f"Number of claws: {len(claws)}")
for claw in claws:
    system = [[[claw[0][0], claw[1][0]], [claw[0][1], claw[1][1]]], claw[2]]
    results = []
    for i in range(101):
        mod1 = (system[1][0] - i * system[0][0][0]) % system[0][0][1]
        mod2 = (system[1][1] - i * system[0][1][0]) % system[0][1][1]
        if mod1 == 0 and mod2 == 0:
            bs = (system[1][0] - i * system[0][0][0]) / system[0][0][1]
            results.append((i, bs))
    results = [res for res in results if res[1] >= 0 and res[1] <= 100]
    costs = [res[0] * A + res[1] * B for res in results]

    if len(costs) > 0:
        cost += min(costs)

print(cost)
