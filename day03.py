import re
prog = open(0).read().replace("\n", ' ')
part1 = sum(int(i)* int(j) for i, j in (m.groups() for m in re.finditer(r"mul\((\d+),(\d+)\)", prog)))
part2 = sum(int(i) * int(j) for i, j in (m.groups() for m in re.finditer(r"mul\((\d+),(\d+)\)",
                                                                        re.sub(r"don't\(\).*?(do\(\)|$)", "", prog)
                                                                        )))
print(part1)
print(part2)
            
