with open('input.txt', 'r') as f:
    arr = f.read().rstrip("\n").split("\n")

code = [] 
val = 5

for cmd in arr:
    for char in cmd:
        if char == "U" and val not in [1,2,3]:
            val -= 3
        if char == "D" and val not in [7,8,9]:
            val += 3
        if char == "L" and val not in [1,4,7]: 
            val -= 1
        if char == "R" and val not in [3,6,9]:
            val += 1 

    code.append(val)

print('Part 1:',''.join([str(x) for x in code])) 

r0 = [0]*7
r1 = [0,0,0,1,0,0,0]
r2 = [0,0,2,3,4,0,0]
r3 = [0,5,6,7,8,9,0]
r4 = [0,0,'A','B','C',0,0]
r5 = [0,0,0,'D',0,0,0]
r6 = [0]*7

pad = [r0,r1,r2,r3,r4,r5,r6] 

i = 3
j = 1

code = []

for cmd in arr:
    for char in cmd:
        ii = i 
        jj = j
        
        if char == 'U':
            ii -= 1 
        if char == 'D':
            ii += 1 
        if char == 'L':
            jj -= 1 
        if char == 'R':
            jj += 1 
        
        if pad[ii][jj] != 0:
            i = ii
            j = jj

    button = pad[i][j]
    code.append(button)

print("Part 2:",''.join([str(x) for x in code])) 
