from time import sleep
from queue import Queue
from hashlib import md5
from itertools import compress
inp = "edjrjqaa" 

def get_pos(path):
    x = path.count('R') - path.count('L')
    y = path.count('D') - path.count('U')

    return x,y

def get_valid(path):
    global inp
    s = inp + path
    m = md5(s.encode()).hexdigest()[:4]
    
    ret = [] 
    for ch in m:
        if 'b' <= ch <= 'f':
            ret.append(True)
        else:
            ret.append(False)
 
    x,y = get_pos(path) 
    if y == 0: ret[0] = False
    if y == 3: ret[1] = False
    if x == 0: ret[2] = False
    if x == 3: ret[3] = False

    return ret


paths = Queue()
paths.put('')

valid_paths = []

while True:
    if paths.empty(): break

    cur = paths.get() 
    if get_pos(cur) == (3,3):
        # print(cur) 
        # break 
        valid_paths.append(cur)
        continue

    f = get_valid(cur) 
    new_paths = list(compress([cur+'U', cur+'D', cur+'L', cur+'R'],f))

    for p in new_paths:
        paths.put(p)

print(len(valid_paths[-1]))





