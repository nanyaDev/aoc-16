import hashlib

with open('input.txt') as f:
    door = f.read().rstrip("\n")

# pw = ""
pw = [None]*8
i = 0
while None in pw: 
    string = door + str(i)
    hash = hashlib.md5(string.encode('utf-8')).hexdigest()

    if hash[:5] == "0" * 5:
        try: # idk if this is good coding practice
            pos = int(hash[5])
        except Exception:
            i += 1
            continue

        if 0 <= pos <=7 and pw[pos] == None:
            pw[pos] = hash[6]

    i += 1

print(''.join(pw))
    
