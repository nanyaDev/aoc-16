import re
from itertools import permutations

string = "abcdefgh"

with open('input.txt') as f:
    inp = f.read().splitlines()

def permute(s):
    global inp
    code = list(s)

    for cmd in inp:
        if 'swap position' in cmd: 
            nums = re.findall(r"\d+",cmd)
            i,j = list(map(int,nums)) 
            code[i],code[j] = code[j],code[i] 
        if 'swap letter' in cmd:
            a,b = re.findall(r"letter (\w)",cmd)
            x = a + b
            y = b + a
            code = [a if ch == b else b if ch == a else ch for ch in code] 
        if 'rotate left' in cmd:
            n = re.findall(r"\d",cmd)[0]
            for _ in range(int(n)):
                ch = code.pop(0)
                code.append(ch)
        if 'rotate right' in cmd:
            n = re.findall(r"\d",cmd)[0]
            for _ in range(int(n)):
                ch = code.pop()
                code.insert(0,ch)
        if 'rotate based on' in cmd:
            ltr = re.findall(r"letter (\w)",cmd)[0]
            n = code.index(ltr)
            n += 1 if n < 4 else 2
            for _ in range(n):
                ch = code.pop()
                code.insert(0,ch)
        if 'reverse' in cmd:
            nums = re.findall(r"\d+",cmd) 
            i,j = list(map(int,nums)) 
            code[i:j+1] = code[i:j+1][::-1]
        if 'move' in cmd:
            nums = re.findall(r"\d+",cmd)
            i,j = list(map(int,nums)) 
            ch = code.pop(i)
            code.insert(j,ch) 

    return "".join(code)

print("Part 1:",permute(string))

perms = ["".join(p) for p in permutations(string)]
for s in perms:
    if permute(s) == "fbgdceah":
        print("Part 2:",s)
        break

    





