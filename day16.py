s = "01111001100111011"
l = 272
l = 35651584 

while len(s) < l:
    a = s
    acp = a[::-1]

    b = int(acp,2) ^ (2 ** (len(acp) + 1) - 1) 
    b = str(bin(b))[3:]
    b = b.rjust(len(a),'1')

    s = a + '0' + b
    print(len(s))

s = s[:l]

while True:
    acc = ""
    for i in range(0,len(s),2):
        if s[i] == s[i+1]:
            acc += '1'
        else:
            acc += '0'

    s = acc 
    if len(s)%2 == 1: break

print(s)


