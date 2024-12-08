import itertools


class Position:
    def __init__(self, *args):
        if len(args) == 1:
            self.row = args[0][0]
            self.col = args[0][1]
        elif len(args) == 2:
            self.row = args[0]
            self.col = args[1]
        else:
            raise ValueError("Init problem")

    def __repr__(self) -> str:
        return f"Position(row={self.row}, col={self.col})"

    def isinside(self, rows: int, cols: int) -> bool:
        if self.row < 0 or self.col < 0 or self.row >= rows or self.col >= cols:
            return False
        return True

    def __sub__(self, other):
        if isinstance(other, Position):
            return (self.row - other.row, self.col - other.col)
        if isinstance(other, tuple):
            return (self.row - other[0], self.col - other[1])
        raise ValueError("The other object also has to be a Position or a tuple")

    def __add__(self, other):
        if isinstance(other, Position):
            return (self.row + other.row, self.col + other.col)
        elif isinstance(other, tuple):
            return (self.row + other[0], self.col + other[1])
        raise ValueError("The other object also has to be a Position or a tuple.")

    def __hash__(self):
        return hash(self.row) + hash(self.col)

    def __eq__(self, other):
        if not isinstance(other, Position):
            raise NotImplementedError
        return (self.row, self.col) == (other.row, other.col)


class Frequency:
    def __init__(self, positions: set[Position], rows: int, cols: int):
        self.positions = positions
        self.antidotes = set()
        self.rows = rows
        self.cols = cols

    def add_position(self, position: Position):
        self.positions.add(position)

    def __repr__(self) -> str:
        return f"Positions: {self.positions}\nAntidotes: {list(self.antidotes)}\n"

    def find_antidotes(self):
        if len(self.antidotes) > 0:
            self.antidotes = set()
        if len(self.positions) <= 1:
            return

        combs = list(itertools.combinations(self.positions, 2))

        for comb in combs:
            dir1 = comb[0] - comb[1]
            dir2 = comb[1] - comb[0]

            antidote1 = Position(comb[0] + dir1)
            antidote2 = Position(comb[1] + dir2)
            if antidote1 not in self.positions and antidote1.isinside(
                self.rows, self.cols
            ):
                self.antidotes.add(antidote1)
            if antidote2 not in self.positions and antidote2.isinside(
                self.rows, self.cols
            ):
                self.antidotes.add(antidote2)

    def find_antidotes2(self):
        if len(self.antidotes) > 0:
            self.antidotes = set()
        if len(self.positions) <= 1:
            return

        combs = list(itertools.combinations(self.positions, 2))

        for comb in combs:
            dir1 = comb[0] - comb[1]
            dir2 = comb[1] - comb[0]

            curr_pos1 = Position(comb[0].row, comb[0].col)
            # move in dir 1 until out of bounds
            while True:
                antidote1 = Position(curr_pos1 + dir1)
                if antidote1.isinside(self.rows, self.cols):
                    self.antidotes.add(antidote1)
                    curr_pos1 = Position(antidote1.row, antidote1.col)
                else:
                    break
            curr_pos2 = Position(comb[1].row, comb[1].col)
            # move in dir 2 until out of bounds
            while True:
                antidote2 = Position(curr_pos2 + dir2)
                if antidote2.isinside(self.rows, self.cols):
                    self.antidotes.add(antidote2)
                    curr_pos2 = Position(antidote2.row, antidote2.col)
                else:
                    break


def solve(inp, part2=False):
    frequencies = {}

    for row in range(len(inp)):
        for col in range(len(inp[row])):
            c = inp[row][col]
            if c != ".":
                if c not in frequencies:
                    frequencies[c] = Frequency(
                        set([Position(row, col)]), len(inp), len(inp[row])
                    )
                else:
                    frequencies[c].add_position(Position(row, col))

    antidotes = set()
    for value, frequency in frequencies.items():
        if part2:
            frequency.find_antidotes2()
        else:
            frequency.find_antidotes()
        for antidote in frequency.antidotes:
            if part2:
                for pos in frequency.positions:
                    antidotes.add(pos)
                antidotes.add(Position(antidote.row, antidote.col))
            else:
                if inp[antidote.row][antidote.col] != value:
                    antidotes.add(Position(antidote.row, antidote.col))

    if part2:
        print(f"Part 2: {len(antidotes)}")
    else:
        print(f"Part 1: {len(antidotes)}")


def main():
    with open("input.txt", "r") as fp:
        inp = [line.strip() for line in fp]

    solve(inp=inp)
    solve(inp=inp, part2=True)


if __name__ == "__main__":
    main()
