import pytest
from itertools import chain

TEST_INPUT = (
    "2333133121414131402",
    1928,
    0,
)


def parse(input_str):
    return [*map(int, input_str)]


def solve(input_str, part=1):
    data = parse(input_str)
    f, b = data[0::2], data[1::2]
    rit = reversed([*chain.from_iterable([i] * n for i, n in enumerate(f))])
    res = []
    max_len = sum(f)
    for i, blocks in enumerate(f):
        res.extend(i for _ in range(blocks))
        res.extend(next(rit, None) for _ in range(b[i]))
        if len(res) >= max_len:
            break
    return sum(i * j for i, j in enumerate(res[:max_len]))
        

def test_parse():
    input_str, p1, p2 = TEST_INPUT
    data = parse(input_str)
    assert (len(data) % 2) == 1


def test_example():
    input_str, p1, p2 = TEST_INPUT
    assert solve(input_str, 1) == p1
    if p2:
        assert solve(input_str, 2) == p2


if __name__ == "__main__":
    input_str = open(0).read().strip()
    print(solve(input_str, part=1))
