def part1(arr, curr_dir, xc, yc):
    for x in arr: 
        curr_dir += 1 if x[0] == 'R' else -1
        curr_dir %= 4 

        val = int(x[1:]) 
        if curr_dir == 0:
            yc += val
        elif curr_dir == 1:
            xc += val
        elif curr_dir == 2:
            yc -= val
        elif curr_dir == 3:
            xc -= val

    return xc,yc

def part2(arr, curr_dir, xc, yc, visited): 
    for x in arr: 
        curr_dir += 1 if x[0] == 'R' else -1
        curr_dir %= 4 

        val = int(x[1:]) 
        for _ in range(val):
            if curr_dir == 0:
                yc += 1
            elif curr_dir == 1:
                xc += 1
            elif curr_dir == 2:
                yc -= 1
            elif curr_dir == 3:
                xc -= 1
            
            if [xc,yc] in visited:
                return xc,yc
            else:
                visited.append([xc,yc])


with open('input.txt', 'r') as f:
    arr = f.read().rstrip("\n").split(", ")

# main()
dir = ['n', 'e', 's', 'w']
curr_dir = 0
xc = 0
yc = 0
visited = [[xc,yc]]

x,y = part1(arr, curr_dir, xc, yc)
print(abs(x) + abs(y))

x,y = part2(arr, curr_dir, xc, yc, visited)
print(abs(x) + abs(y))

