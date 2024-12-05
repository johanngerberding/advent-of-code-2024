import functools

test = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

test = test.split()
test_rules = [[int(n) for n in el.split("|")] for el in test if "|" in el]
test_updates = [[int(n) for n in el.split(",")] for el in test if "|" not in el]


def solve(rules: list, updates: list, part: str):
    def validate_rules(num: int, before: list[int], after: list[int]) -> bool:
        for rule in rules:
            if num in rule:
                if num == rule[0]:
                    if rule[1] in before:
                        return False
                else:
                    if rule[0] in after:
                        return False
        return True

    good_updates = []
    for update in updates:
        bad = False
        before = []
        after = update[1:]
        for i in range(len(update)):
            if not validate_rules(update[i], before, after):
                bad = True
                break
            before.append(update[i])
            if len(after) > 0:
                after.pop(0)
        if not bad:
            good_updates.append(update)

    middle_sum = 0
    for update in good_updates:
        middle = len(update) // 2
        middle_sum += update[middle]

    print(f"{part}: {middle_sum}")


solve(test_rules, test_updates, "Test")


with open("input.txt", "r") as fp:
    data = fp.readlines()

data = [el.strip() for el in data]
data = [el for el in data if el != ""]
rules = [[int(n) for n in el.split("|")] for el in data if "|" in el]
updates = [[int(n) for n in el.split(",")] for el in data if "|" not in el]

solve(rules, updates, "Part 1")


### PART 2 ###
def compare(item1, item2):
    if [item1, item2] in rules:
        return -1
    elif [item2, item2] in rules:
        return 1
    return 0


def validate_rules(num: int, before: list[int], after: list[int]) -> bool:
    for rule in rules:
        if num in rule:
            if num == rule[0]:
                if rule[1] in before:
                    return False
            else:
                if rule[0] in after:
                    return False
    return True


bad_updates = []
for update in updates:
    bad = False
    before = []
    after = update[1:]
    for i in range(len(update)):
        if not validate_rules(update[i], before, after):
            bad = True
            break
        before.append(update[i])
        if len(after) > 0:
            after.pop(0)
    if bad:
        bad_updates.append(update)

middle_sum = 0
for update in bad_updates:
    update.sort(key=functools.cmp_to_key(compare))
    middle = len(update) // 2
    middle_sum += update[middle]

print(f"part2: {middle_sum}")
