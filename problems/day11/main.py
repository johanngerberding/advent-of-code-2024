example = "125 17"

example = [int(el) for el in example.split(" ")]

with open("input.txt", "r") as fp:
    example = [int(el) for el in fp.read().split(" ")]


for _ in range(25):
    temp = []
    for el in example:
        if el == 0:
            temp.append(1)
        elif len(str(el)) % 2 == 0:
            split = len(str(el)) // 2
            temp.append(int(str(el)[:split]))
            temp.append(int(str(el)[split:]))
        else:
            temp.append(el * 2024)
    example = temp

print(len(example))
