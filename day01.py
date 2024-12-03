import re
import sys
digits = [int(i) for i in re.findall(r"\d+", sys.stdin.read())]
left = sorted(digits[::2])
right = sorted(digits[1::2])
print(sum(abs(i - j) for i, j in zip(left, right)))
print(sum(j * sum(j == i for i in right) for j in left))
