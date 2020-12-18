with open('input.txt', 'r') as f:
    inp = f.read().rstrip("\n").split("\n")

arr = [list(map(int,x.split())) for x in inp]

def check_tris(arr):
    count = 0
    for item in arr:
        l = sorted(item)
        if l[0] + l[1] > l[2]:
            count += 1
    return count

print(check_tris(arr))

cols = list(zip(*arr))
big_arr = [item for col in cols for item in col]
tris = [big_arr[i:i+3] for i in range(0,len(big_arr),3)]

print(check_tris(tris))
