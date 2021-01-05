with open('input.txt') as f:
    inp = f.read().splitlines()

bounds = [list(map(int,i.split("-"))) for i in inp]
bounds.sort()

i = 0
while i < len(bounds) - 1:
    s1,e1 = bounds[i]
    s2,e2 = bounds[i+1]

    if e1 < s2 - 1:
        i += 1
    else:
        bounds[i][1] = max(e1,e2)
        del bounds[i+1]

print("Part 1:",bounds[0][1] + 1)

count = 2**32
for start,end in bounds:
    count -= (end - start + 1)

print("Part 2:",count)




