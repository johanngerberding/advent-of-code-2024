with open("input.txt", "r") as fp:
    inp = fp.readlines()

inp = [el.strip() for el in inp]

# inp = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""
# inp = inp.split()


class Simulation:
    def __init__(
        self,
        inp: list,
        curr_dir: int = 0,
        current: tuple | None = None,
        visited: set | None = None,
    ):
        self.inp = inp
        self.curr_dir = curr_dir
        self.incrementers = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        if not current:
            self._get_start()
        else:
            self.current = current
        if not visited:
            self.visited = set([self.current])
        else:
            self.visited = visited

    def _get_start(self):
        for row in range(len(self.inp)):
            for col in range(len(self.inp[row])):
                if self.inp[row][col] == "^":
                    self.current = (row, col, self.curr_dir)
                    return

    def _step(self):
        next_position = self._get_next()
        if not self._inside(next_position):
            # we are done
            return False

        while self.inp[next_position[0]][next_position[1]] == "#":
            # switch direction
            self._switch_dir()
            next_position = self._get_next()

        # set new position
        self.current = next_position
        self.visited.add(self.current)
        return True

    def simulate(self):
        while self._step():
            continue

    def _switch_dir(self):
        self.curr_dir += 1
        if self.curr_dir > 3:
            self.curr_dir = 0

    def _inside(self, pos: tuple) -> bool:
        return not (
            pos[0] < 0
            or pos[0] >= len(self.inp)
            or pos[1] < 0
            or pos[1] >= len(self.inp[0])
        )

    def _get_next(self) -> tuple:
        return (
            self.current[0] + self.incrementers[self.curr_dir][0],
            self.current[1] + self.incrementers[self.curr_dir][1],
        )


part1 = Simulation(inp=inp)
part1.simulate()
print(f"Part 1: {len(set([(el[0], el[1]) for el in part1.visited]))}")

obs = 0
part2 = Simulation(inp=inp)
while part2._step():
    start = part2.current  # now I need a switch to the right
    direction = part2.curr_dir
    if direction > 3:
        direction = 0
    start = (start[0], start[1], direction)
    visited = part2.visited
    visited.add(start)
    subsim = Simulation(inp=inp, curr_dir=direction, current=start, visited=visited)
    while subsim._step():
        if subsim.current in subsim.visited:
            obs += 1
            break

print(obs)
