from collections import defaultdict

grid = defaultdict(str) | {
    x + y * 1j: c
    for y, line in enumerate(open(0).read().splitlines())
    for x, c in enumerate(line)
}
(init_pos,) = (z for z, c in grid.items() if c == "^")


def walk():
    pos = init_pos
    visited = set()
    d = -1j
    while grid[pos]:
        if (pos, d) in visited:
            return 1, visited
        visited.add((pos, d))
        if grid[next_pos := pos + d] == "#":
            d *= 1j
        else:
            pos = next_pos
    return 0, visited


_, visited = walk()
print(f"Part 1: {len({z for z, _ in visited})}")


def part2():
    count = 0
    for position in {z for z, _ in visited if z != init_pos}:
        grid[position] = "#"
        loop, _ = walk()
        count += loop
        grid[position] = "."
    print(count)


part2()
