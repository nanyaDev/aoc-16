inp = ".^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^."
rows = 40       # part 1
rows = 400000   # part 2

arr = [inp]
prev = inp
for _ in range(rows-1):
    prev_dict = { i:prev[i] for i in range(len(prev)) }
    prev_dict[-1] = "."
    prev_dict[len(prev)] = "."

    cur = "." * len(inp) 
    cur = list(cur)
    for i in range(len(cur)):
        b1 = prev_dict[i-1] == "^" and prev_dict[i] == "^" and prev_dict[i+1] == "."
        b2 = prev_dict[i-1] == "." and prev_dict[i] == "^" and prev_dict[i+1] == "^"
        b3 = prev_dict[i-1] == "^" and prev_dict[i] == "." and prev_dict[i+1] == "."
        b4 = prev_dict[i-1] == "." and prev_dict[i] == "." and prev_dict[i+1] == "^"

        if b1 or b2 or b3 or b4:
            cur[i] = "^"

    cur = "".join(cur) 
    arr.append(cur)

    prev = cur

count = 0
for row in arr:
    count += row.count(".")

print(count)


