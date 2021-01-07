with open('input.txt') as f:
    inp = f.read().rstrip().split("\n")
    inp = [x.split(' ') for x in inp]

def i(ch):
    mp = ch.maketrans("abcd", "0123")
    return int(ch.translate(mp))


reg = [7,0,0,0] # part 1
reg = [12,0,0,0] # part 2

j = 0 
while j < len(inp):
    cmd = inp[j]

    # peephole optimization
    # note: should account for tgl for general case
    if j == 4:
        reg[0] += (reg[1]) * (reg[3])
        reg[2] = 0
        reg[3] = 0 
        j += 6
        continue
    if j == 15:
        reg[2] += reg[3] if inp[14][0] == 'inc' else -reg[3]
        reg[3] = 0
        j += 1
        continue
    if j == 23:
        reg[0] += reg[3] if inp[21][0] == 'inc' else -reg[3] # += instead of -= bc the previous 'inc d' gets toggled
        reg[3] = 0
        j += 1
        continue

    if cmd[0] == 'inc':
        if 'a' <= cmd[1] <= 'd': # exclude invalid instructions
            reg[i(cmd[1])] += 1
    elif cmd[0] == 'dec':
        if 'a' <= cmd[1] <= 'd': # exclude invalid instructions
            reg[i(cmd[1])] -= 1
    elif cmd[0] == 'cpy':
        if 'a' <= cmd[2] <= 'd': # exclude invalid instructions
            if 'a' <= cmd[1] <= 'd':
                reg[i(cmd[2])] = reg[i(cmd[1])]
            else:
                reg[i(cmd[2])] = int(cmd[1])
    elif cmd[0] == 'jnz':
        if 'a' <= cmd[1] <= 'd':
            n = reg[i(cmd[1])]
        else:
            n = int(cmd[1])

        if 'a' <= cmd[2] <= 'd':
            m = reg[i(cmd[2])]
        else:
            m = int(cmd[2])

        if (n != 0):
            j += m
            continue
    elif cmd[0] == 'tgl':
        n = reg[i(cmd[1])]

        if j+n >= len(inp) or j+n < 0: 
            j += 1
            continue
        if inp[j+n][0] == 'inc': 
            inp[j+n][0] = 'dec'
        elif inp[j+n][0] == 'dec' or inp[j+n][0] == 'tgl': 
            inp[j+n][0] = 'inc'
        elif inp[j+n][0] == 'cpy': 
            inp[j+n][0] = 'jnz'
        elif inp[j+n][0] == 'jnz': 
            inp[j+n][0] = 'cpy' 
    j += 1

print(reg[0]) 
