from queue import Queue
from time import sleep

inp = 1362
target = (31,39)

def is_open(coord):
    x,y = coord
    global inp

    n = x*x + 3*x + 2*x*y + y + y*y + inp
    n1 = bin(n).count("1")

    return True if n1 % 2 == 0 else False


q = Queue()
visited = set()
dist = {}

q.put((1,1))
visited.add((1,1))
dist[(1,1)] = 0

while not q.empty():
    coord = q.get()

    if dist[coord] == 50:
        continue
    # if coord == target:
    #     print(dist[coord])
    #     break

    x,y = coord
    n = (x+1,y)
    e = (x,y+1)
    s = (x-1,y)
    w = (x,y-1)

    cur_dist = dist[coord]
    for dir in [n,e,s,w]:
        if is_open(dir) and dir not in visited and dir[0] >= 0 and dir[1] >= 0:
            q.put(dir)
            visited.add(dir)
            dist[dir] = cur_dist + 1

print(len(visited))

