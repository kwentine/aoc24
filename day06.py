d = -1j
visited = set()
obstacles = set()
free = set()

for k, line in enumerate(open(0).readlines()):
    for i, c in enumerate(line.strip()):
        if c == '^':
            init_pos = complex(i, k)
        if c == '#':
            obstacles |= {complex(i, k)}

def is_out(pos):
    x, y = pos.real, pos.imag
    return not (0 <= x <= i and 0 <= y <= k)

def walk(init_pos, obstacles):
    visited = set()
    pos = init_pos
    d = -1j 
    while not is_out(pos):
        if (pos, d) in visited:
            raise ValueError("Loop!")
        visited.add((pos, d))
        if pos + d in obstacles:
            d *= 1j
        else:
            pos = pos + d
    return {p for p, d in visited}

path = walk(init_pos, obstacles)
print(len(path))

count = 0

for position in path - {init_pos}:
    try:
        walk(init_pos, obstacles | {position})
    except ValueError:
        count += 1
        print(f"Progress: {count}")
print(count)

