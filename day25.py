from time import sleep

with open('input.txt') as f:
    inp = f.read().rstrip().split("\n")
    inp = [x.split(' ') for x in inp]

def i(ch):
    mp = ch.maketrans("abcd", "0123")
    return int(ch.translate(mp))

a = 0
while True:
    reg = [a,0,0,0]
    exp_out = 0

    j = 0
    count = 0
    while j < len(inp):
        cmd = inp[j]
        if count > 100:
            print(a)
            exit()

        if cmd[0] == 'inc':
            reg[i(cmd[1])] += 1
        elif cmd[0] == 'dec':
            reg[i(cmd[1])] -= 1
        elif cmd[0] == 'cpy':
            if 'a' <= cmd[1] <= 'd':
                reg[i(cmd[2])] = reg[i(cmd[1])]
            else:
                reg[i(cmd[2])] = int(cmd[1])
        elif cmd[0] == 'jnz':
            if 'a' <= cmd[1] <= 'd':
                n = reg[i(cmd[1])]
            else:
                n = int(cmd[1])
            if (n != 0):
                j += int(cmd[2])
                continue
        elif cmd[0] == 'out':
            n = reg[i(cmd[1])]
            if n == exp_out:
                exp_out = exp_out * -1 + 1
                count += 1
            else:
                break

        j += 1 
    a += 1


