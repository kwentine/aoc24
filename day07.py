import pytest
from re import findall
from operator import add, mul

TEST_INPUT = (
    """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""",
    3749,
    11387,
)


def satisfy(target, equation, part=1):
    todo = [[*reversed(equation)]]
    while todo:
        values = todo.pop()
        left = values.pop()
        right = values.pop()
        for val in [left + right, left * right, int(f"{left}{right}")][: part + 1]:
            if val == target and all(v == 1 for v in values):
                return True
            if val < target and values:
                todo.append(values + [val])
    return False


def parse(input_str):
    return [
        (int(target), [*map(int, equation.split())])
        for target, equation, _ in findall(r"(\d+): ((\d+\s)+)", input_str)
    ]


def solve(input_str, part=1):
    return sum(t for t, e in parse(input_str) if satisfy(t, e, part))


def test_example():
    input_str, p1, p2 = TEST_INPUT
    assert solve(input_str, 1) == p1
    if p2:
        assert solve(input_str, 2) == p2


@pytest.mark.parametrize(
    "t,e,r",
    [
        (11, [7, 3, 1], 1),
        (10, [7, 3, 1], 1),
        (12, [7, 3, 1], 0),
        (1, [1, 1], 1),
        (1, [2, 1], 0),
        (12350, [5, 1, 40, 200, 9, 8, 9, 3, 5, 1, 6, 2], 1),
    ],
)
def test_satisfy(t, e, r):
    assert satisfy(t, e) == r


if __name__ == "__main__":
    input_str = open(0).read()
    print(solve(input_str, 1))
    print(solve(input_str, 2))
