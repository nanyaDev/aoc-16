import re

with open('input.txt') as f:
    arr = f.read().rstrip("\n").split("\n")

data = []
hypernet = []

for s in arr: 
    data.append(re.split("\[\w+\]",s))
    hypernet.append(re.findall("\[(\w+)\]", s))

def check_abba(s):
    l = len(s)
    if l < 4:
        return False 
    
    for i in range(l-3):
        a,b,c,d = s[i:i+4]
        if a == d and b == c and a != b:
            return True
    
    return False

def get_aba_arr(arr):
    ret = set()
    
    for s in arr:
        l = len(s)
        if l < 3:
            return [] 
        
        for i in range(l-2):
            a,b,c = s[i:i+3]
            if a == c and a != b:
                ret.add(s[i:i+3])
        
    return list(ret)

def aba_to_bab(arr):
    ret = []
    for aba in arr:
        a,b,c = aba
        ret.append(b + a + b)

    return ret 

count = 0
for i in range(len(arr)):
    flag = False
    for s in data[i]:
        if check_abba(s):
            flag = True

    for s in hypernet[i]:
        if check_abba(s):
            flag = False

    if flag:
        count += 1

print(count)

count = 0

count = 0
for i in range(len(arr)):
    aba_arr = get_aba_arr(data[i])
    bab_arr = aba_to_bab(aba_arr)

    flag = False
    for s in hypernet[i]:
        for bab in bab_arr:
            if bab in s:
                count += 1
                flag = True
                break
        if flag:
            break

print(count)

