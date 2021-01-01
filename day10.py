import re
from collections import defaultdict

with open('input.txt') as f:
    inp = f.read().rstrip().split("\n")

arr = []
for line in inp:
    m = re.findall("\w+ \d+",line)
    acc = []
    for s in m:
        st, num = s.split(" ")
        ret = [st, int(num)]
        acc.append(ret)
    arr.append(acc)

bot_vals = defaultdict(list)
output_vals = defaultdict(list)
for item in arr: 
    if item[0][0] == 'value':
        val = item[0][1]
        bot = item[1][1]
        bot_vals[bot].append(val)
while True:
    for item in arr:
        if item[0][0] != 'value':
            bot,low,high = item[0][1], item[1][1], item[2][1] 
            if len(bot_vals[bot]) < 2:
                next
            else:
                l,h = sorted(bot_vals[bot])
                
                # part 1:
                # if l == 17 and h == 61:
                #     print(bot)
                #     flag = True
                #     break

                
                if item[1][0] == 'bot':
                    bot_vals[low].append(l)
                else:
                    output_vals[low].append(l)

                if item[2][0] == 'bot':
                    bot_vals[high].append(h)
                else:
                    output_vals[high].append(h)

                bot_vals[bot] = [] 

                a = output_vals[0]
                b = output_vals[1]
                c = output_vals[2]

                if a and b and c:
                    print(a[0]*b[0]*c[0])
                    exit()

