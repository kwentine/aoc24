import pytest
TEST_INPUT = (
    """\
""",
    0,
    0,
)


def parse(input_str):
    pass


def solve(input_str, part=1):
    pass


def test_parse():
    from pprint import pprint
    pprint(parse(TEST_INPUT[0]))


def test_example():
    input_str, p1, p2 = TEST_INPUT
    assert solve(input_str, 1) == p1
    if p2:
        assert solve(input_str, 2) == p2


if __name__ == "__main__":
    try:
        test_example()
    except AssertionError as e:
        print(f"Failed example: {e}")
    input_str = open(0).read()
    assert input_str[:-1] == "\n"
    print(solve(input_str, part=1))
