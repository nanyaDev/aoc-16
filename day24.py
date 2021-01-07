from queue import Queue
import math
from itertools import permutations

with open('input.txt') as f:
    grid = list(map(list,f.read().splitlines()))

nums = [None] * 8

for i,row in enumerate(grid):
    for j,ch in enumerate(row):
        if '0' <= ch <= '7':
            nums[int(ch)] = [i,j]


# min_pairs = [[None] * 8] * 8 # this causes the outer list items to all reference the same list
min_pairs = [[None] * 8 for _ in range(8)]

for n,[i_s,j_s] in enumerate(nums): 
    visited = []
    q = Queue()
    q.put([i_s,j_s,0])

    while not q.empty():
        i,j,d = q.get()

        if [i,j] in visited:
            continue
        else:
            visited.append([i,j])


        if '0' <= grid[i][j] <= '7':
            min_pairs[n][int(grid[i][j])] = d

        if i > 0 and grid[i-1][j] != '#':
            q.put([i-1,j,d+1])
        if i < len(grid)-1 and grid[i+1][j] != '#':
            q.put([i+1,j,d+1])
        if j > 0 and grid[i][j-1] != '#':
            q.put([i,j-1,d+1])
        if j < len(grid[0])-1 and grid[i][j+1] != '#':
            q.put([i,j+1,d+1])

min_sum = math.inf
# is there a non bruite force way to solve this route optimization problem?
for perm in permutations(range(1,8)):
    sum = 0
    cur_node = 0
    for node in perm:
        sum += min_pairs[cur_node][node]
        cur_node = node

    # part 2 line
    sum += min_pairs[cur_node][0]

    if sum < min_sum: min_sum = sum

print(min_sum)


