import sys, re
safe = 0
almost_safe = 0
is_safe = lambda l: all(0 < x < 4 for x in l) or all(-4 < x < 0  for x in l)
for line in sys.stdin.readlines():
    levels = [*map(int, re.findall(r"-?\d+", line))]
    incr = [i - j for i, j in zip(levels[:-1], levels[1:])]
    candidates = [incr[1:], incr[:-1], *(incr[:i] + [incr[i] + incr[i + 1]] + incr[i + 2:] for i in range(len(incr) - 1))]
    safe += is_safe(incr)
    almost_safe +=  any(is_safe(c) for c in candidates)
print(safe)
print(almost_safe)
