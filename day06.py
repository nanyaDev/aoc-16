with open('input.txt') as f:
    arr = f.read().rstrip("\n").split("\n")

cols = list(zip(*arr))

msg = []
for col in cols: 
    ret = min(set(col),key=col.count)
    msg.append(ret)

ans = ''.join(msg)
print(ans)
        

