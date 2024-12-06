from re import findall
from collections import defaultdict
rules, updates = open(0).read().split("\n\n")
prereqs = defaultdict(set)
for before, after in findall(r"(\d+)\|(\d+)", rules):
    prereqs[int(after)] |= {int(before)}


def check(update):
    return not any(prereqs[n] & set(update[i + 1:])
                   for i, n in enumerate(update))

def swap(i, j, seq):
    return [j if k == i else i if k == j else k for k in seq]

def sort(seq):
    while 1:
        for i, n in enumerate(seq):
            p = prereqs[n]
            swap_with = None
            for m in seq[-1:i:-1]:
                if m in p:
                    swap_with = m
                    break
            if swap_with is not None:
                seq = swap(n, m, seq)
                break
        else:
            break
    return seq

valid = 0
invalid = 0
for line in updates.splitlines():
    update = [*map(int, findall(r"\d+", line))]
    seq = sort(update)
    assert len(seq) == len(update)
    assert check(seq)
    valid += (seq == update) * update[len(update) // 2]
    invalid += (seq != update) * seq[len(seq) // 2]

print(valid, invalid)
