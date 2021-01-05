from collections import deque

inp = 3_012_210
elf = [i+1 for i in range(inp)]

while len(elf) > 1:
    if len(elf) % 2 == 1:
        del elf[1::2] 
        del elf[0]
    else:
        del elf[1::2] 

print("Part 1:",elf[0])

mid = inp//2 + 1
q1 = deque(range(1,mid))
q2 = deque(range(mid,inp+1))

even = True
while q1 and q2:
    if even:
        q2.popleft()
    else:
        q1.pop()

    q2.append(q1.popleft())
    q1.append(q2.popleft())
    even = not even

print("Part 2:",q1[0])

