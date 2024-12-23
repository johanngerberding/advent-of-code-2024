instruction_pointer = 0

example = """Register A: 64854237
Register B: 0
Register C: 0

Program: 2,4,1,1,7,5,1,5,4,0,5,5,0,3,3,0"""


def parse(inp) -> tuple:
    data = inp.split("\n\n")
    registers = [int(line.split(":")[1].strip()) for line in data[0].split("\n")]
    program = [int(el) for el in data[1].split(":")[1].strip().split(",")]
    program = [(program[i], program[i + 1]) for i in range(0, len(program) - 1, 2)]
    return registers, program


output = []


def operand2literal(operand: int, registers: list) -> int:
    if operand <= 3:
        return operand
    if operand == 4:
        return registers[0]
    if operand == 5:
        return registers[1]
    if operand == 6:
        return registers[2]
    if operand == 7:
        return operand
    raise ValueError(f"Operand {operand} not supported")


def exec(program: list, inst_pointer: int, registers: list) -> int:
    instruction, operand = program[inst_pointer]
    operand = operand2literal(operand, registers)
    if instruction == 0:
        registers[0] = int(registers[0] / 2**operand)
        return inst_pointer + 1
    elif instruction == 1:
        registers[1] = registers[1] ^ operand
        return inst_pointer + 1
    elif instruction == 2:
        registers[1] = operand % 8
        return inst_pointer + 1
    elif instruction == 3:
        if registers[0] == 0:
            return inst_pointer + 1
        print(f"lets jump to {operand}")
        return operand
    elif instruction == 4:
        registers[1] = registers[1] ^ registers[2]
        return inst_pointer + 1
    elif instruction == 5:
        output.append(operand % 8)
        return inst_pointer + 1
    elif instruction == 6:
        registers[1] = int(registers[0] / 2**operand)
        return inst_pointer + 1
    elif instruction == 7:
        registers[2] = int(registers[0] / 2**operand)
        return inst_pointer + 1
    raise ValueError(
        f"This instruction {instruction} is not part of the instruction set"
    )


registers, program = parse(inp=example)

print(program)
print(registers)


while instruction_pointer < len(program):
    instruction_pointer = exec(
        program=program, inst_pointer=instruction_pointer, registers=registers
    )

print(output)
print(",".join([str(el) for el in output]))


# 1 Test
output = []
instruction_pointer = 0
registers = [0, 0, 9]
program = [(2, 6)]

while instruction_pointer < len(program):
    instruction_pointer = exec(program, instruction_pointer, registers)

print(registers)

# 2 Test
output = []
instruction_pointer = 0
registers = [10, 0, 0]
program = [(5, 0), (5, 1), (5, 4)]

while instruction_pointer < len(program):
    instruction_pointer = exec(program, instruction_pointer, registers)

print(output)

# 3 Test
output = []
instruction_pointer = 0
registers = [2024, 0, 0]
program = [(0, 1), (5, 4), (3, 0)]

while instruction_pointer < len(program):
    instruction_pointer = exec(program, instruction_pointer, registers)

assert registers[0] == 0

print(output)
print(registers)

# 4 Test
output = []
instruction_pointer = 0
registers = [0, 29, 0]
program = [(1, 7)]

while instruction_pointer < len(program):
    instruction_pointer = exec(program, instruction_pointer, registers)
assert registers[1] == 26
print(registers)

# 4 Test
output = []
instruction_pointer = 0
registers = [0, 2024, 43690]
program = [(4, 0)]

while instruction_pointer < len(program):
    instruction_pointer = exec(program, instruction_pointer, registers)
assert registers[1] == 44354
print(registers)
