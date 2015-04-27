ans = 471186387451848374701282213440713470402895200679708722960352108591145331
s = []
i = 0
while ans > 0:
    s.append(chr(ans & 0xff))
    i += 1
    ans = ans >> 8
c = []
print '===Leve1 Key==='
print ''.join(s)[::-1]
print '==============='

base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)] 

#reverse
def f1(s):
    return s[::-1] 

#bin2dec
def f2(s):
    return str(int(s, 2)) 

#dec2bin
def f3(s):
    s = int(s) 
    mid = [] 
    while True: 
        if s == 0: break
        s,rem = divmod(s, 2) 
        mid.append(base[rem]) 
    return ''.join([str(x) for x in mid[::-1]]) 

#hex2dec
def f4(s):
    return str(int(s.upper(), 16)) 

#dec2hex
def f5(s):
    s = int(s) 
    mid = [] 
    while True: 
        if s == 0: break
        s,rem = divmod(s, 16) 
        mid.append(base[rem]) 
    return ''.join([str(x) for x in mid[::-1]]) 
    
#hex2bin
def f6(s):
    return f3(f4(s.upper())) 

#bin2hex
def f7(s):
    return f5(f2(s))

def f8(s):
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)

    return "".join([d.get(c, c) for c in s])

def f9(s):
    b = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    p = "="
    ret = ""
    left = 0
    for i in range(0, len(s)):
        if left == 0:
            ret += b[ord(s[i]) >> 2]
            left = 2
        else:
            if left == 6:
                ret += b[ord(s[i - 1]) & 63]
                ret += b[ord(s[i]) >> 2]
                left = 2
            else:
                index1 = ord(s[i - 1]) & (2 ** left - 1)
                index2 = ord(s[i]) >> (left + 2)
                index = (index1 << (6 - left)) | index2
                ret += b[index]
                left += 2
    if left != 0:
        ret += b[(ord(s[len(s) - 1]) & (2 ** left - 1)) << (6 - left)]
    for i in range(0, (4 - len(ret) % 4) % 4):
        ret += p
    return ret

def f10(s):
    b = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    p = "="
    ret = ""
    s2 = s.replace(p, "")
    left = 0
    for i in range(0, len(s2)):
        if left == 0:
            left = 6
        else:
            value1 = b.index(s2[i - 1]) & (2 ** left - 1)
            value2 = b.index(s2[i]) >> (left - 2)
            value = (value1 << (8 - left)) | value2
            ret += chr(value)
            left -= 2
    return ret

def f11(n):
    return n.encode("hex")

def f12(n):
    return n.decode("hex")

ans2 = "111010110111010000000001000001110010010011111101111110010011011010010011000001100111100"
ans3 = "AGZ0AQD3A2V3LwqvZmN3MQVjAmp2BGMwAzZlZQLkAmD3AQL1AzH2AQVjA2VmZGqxZwRlZGVkA2D3MN=="

f = [None, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12]
i = 0
s1 = '({0}, {1}, {2}, {3})'
for i1 in range(1, 13):
    for i2 in range(1, 13):
        for i3 in range(1, 13):
            for i4 in range(1, 13):
                try: 
                    p = f[i1](f[i2](f[i3](int(f[i4](ans2)) / 0xddaa)))
                    if len(p) < 11:
                        print '===Leve2 Key==='
                        print s1.format(i1, i2, i3, i4)
                        print p
                        print '==============='
                        break
                except Exception:
                    pass
                    
s2 = '({0}, {1}, {2})'
for i1 in range(1, 13):
    for i2 in range(1, 13):
        for i3 in range(1, 13):
            try: 
                p = f[i1](f[i2](f[i3](ans3)))
                if p[0] == 'S' and p[1] == 'D' and p[2] == 'G':
                    print '===Leve3 Key==='
                    print s2.format(i1, i2, i3)
                    print p
                    print '==============='
                    break
            except Exception:
                pass

