import re

with open('input.txt') as f:
    s = f.read().rstrip("\n") 

def decompress(pos, l):
    global s

    pattern = re.compile(r"\((\d+)x(\d+)\)")
    m = pattern.search(s,pos,pos+l)

    if m == None: return l

    length, n = int(m.group(1)), int(m.group(2))
    offset = m.start() - pos
    rep_sec = n*decompress(m.end(),length)
    og_end = pos + l
    rec_end = m.end() + length
    end_sec = decompress(rec_end,og_end-rec_end)

    return offset + rep_sec + end_sec 
        
ans = decompress(0,len(s))
print(ans)

# part 1

# pos = 0
# while True:
#     pattern = re.compile(r"\((\d+)x(\d+)\)")
#     m = pattern.search(s, pos)
#     if m == None:
#         break
# 
#     ltrs, rpt = int(m.group(1)), int(m.group(2))
#     string_insert = s[m.end():m.end() + ltrs] * (rpt-1)
# 
#     pos = m.start()
#     print(pos)
#     
# print(s)
# print(len(s))


