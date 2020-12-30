import re
from time import sleep

with open('input.txt') as f:
    inp = f.read().rstrip().splitlines()

arr = []
for s in inp:
    nums = re.findall("\d+",s)
    arr.append([int(nums[i]) for i in [0,1,3]])

arr.append([7,11,0]) # part 2
mod_eqs = []
for item in arr:
    n, mod, pos = item
    offset = mod - ((pos + n) % mod)

    mod_eqs.append([offset,mod])

mod_eqs.sort(key = lambda x : x[1])
a = mod_eqs[0][0]
n = mod_eqs[0][1]

for modeq in mod_eqs[1:]:
    rem, mod = modeq

    i = 0; 
    while True:
        ai = a + i*n
        if ai % mod == rem:
            a = ai
            n *= mod
            break
        else:
            i += 1

print(a)

