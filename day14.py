from hashlib import md5
from collections import deque
import re 
from time import sleep

salt = "zpqevtbw"
# salt = "abc"

def get_hash(i, reps=2017):
    global salt
    string = salt + str(i)

    for _ in range(reps):
        string = md5(string.encode()).hexdigest()

    return string

keys = []
index = 0
mem = deque([get_hash(i) for i in range(1001)])

# try to optimize code
while len(keys) < 64:
    if index%1000 == 0: print(index)
    hexhash = mem[0]
    m = re.search(r"(\w)\1\1", hexhash)

    if m != None:
        ltr = m.group(1)
        for i in range(1,1001):
            h = mem[i]

            if re.search(ltr*5, h) != None:
                keys.append(index)
                print(len(keys))
                break 

    index += 1
    mem.popleft()
    mem.append(get_hash(1000+index))

print(keys[-1])
