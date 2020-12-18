import re

with open('input.txt', 'r') as f:
    arr = f.read().rstrip("\n").split("\n")

arr = [re.sub("[-\[\]]", "", code) for code in arr]

valid_rooms = []
count = 0 
for code in arr:
    match = re.match("(\D+)(\d+)(\D+)", code)
    name, sector, checksum = match.groups()
    
    ltrs = {}
    for l in name:
        if l in ltrs:
            ltrs[l] += 1
        else:
            ltrs[l] = 1
    freq = {k:v for k,v in sorted(ltrs.items(), key = lambda x:x[0], reverse = False)}
    freq = [k for k,v in sorted(freq.items(), key = lambda x:x[1], reverse = True)]
    ck = ''.join(freq[:5])

    if ck == checksum:
        count += int(sector)
        valid_rooms.append([name,int(sector)])

decode_list = []
for name, rot in valid_rooms:
    decode_word = []
    for char in name:
        realn = ((ord(char) - ord('a') + rot) % 26) + ord('a')
        real = chr(realn)
        decode_word.append(real)

    decode_list.append([''.join(decode_word),rot])

for name,sector in decode_list:
    if "northpoleobject" in name:
        print(sector)

print(count)
 
    
