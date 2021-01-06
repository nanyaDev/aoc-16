import re

with open('input.txt') as f:
    inp = f.read().splitlines()[2:] 

data = [re.split(r"\s+",item) for item in inp]

ret = 0
for i,a in enumerate(data): 
    ua = int(a[2][:-1])
    aa = int(a[3][:-1])

    if ua == 0: continue

    for j,b in enumerate(data):
        if i == j: continue

        ub = int(b[2][:-1])
        ab = int(b[3][:-1])

        if ua <= ab:
            ret += 1 

print("Part 1:",ret)

display = [[None for _ in range(28)] for _ in range(32)]

for node in inp:
    x,y,sz,us,av,us_p = map(int, re.findall("\d+",node))

    if us_p <= 10:
        display[x][y] = '_' 
    elif us_p >= 90:
        display[x][y] = '#' 
    else:
        display[x][y] = '.'


for i,row in enumerate(display):
    print(str(i).rjust(2),end='')
    print("".join(row))




    
