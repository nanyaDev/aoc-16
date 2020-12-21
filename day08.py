import re

with open('input.txt') as f:
    instructions = f.read().rstrip("\n").split("\n")

rl = 50
cl = 6
screen = [[0]*rl for i in range(cl)]

def parr(arr):
    for row in arr:
        for item in row:
            print(" ",end="") if item == 0 else print(item,end="")
        print("")

def rect(a,b):
    global screen
    for i in range(b):
        for j in range(a):
            screen[i][j] = 1


def rotatey(row,val):
    global screen
    screen[row] = screen[row][-val:] + screen[row][0:-val]

def rotatex(col,val):
    global screen
    
    screen_tr = list(map(list, zip(*screen)))
    screen_tr[col] = screen_tr[col][-val:] + screen_tr[col][0:-val]
    screen = list(map(list, zip(*screen_tr))) 

for ins in instructions: 
    n1, n2 = re.findall("(\d+)", ins)
    n1 = int(n1)
    n2 = int(n2)



    if "rect" in ins:
        rect(n1,n2)
    if "rotate" in ins and "y=" in ins:
        rotatey(n1,n2)
    if "rotate" in ins and "x=" in ins:
        rotatex(n1,n2)

flat_screen = [item for row in screen for item in row]
ret = sum(flat_screen)
print(ret)

parr(screen)
