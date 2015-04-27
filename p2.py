import sys
import os

base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)] 

def f1(s):
    return s[::-1] 

def f2(s):
    return str(int(s, 2)) 

def f3(s):
    s = int(s) 
    mid = [] 
    while True: 
        if s == 0: break
        s,rem = divmod(s, 2) 
        mid.append(base[rem]) 
    return ''.join([str(x) for x in mid[::-1]]) 

def f4(s):
    return str(int(s.upper(), 16)) 

def f5(s):
    s = int(s) 
    mid = [] 
    while True: 
        if s == 0: break
        s,rem = divmod(s, 16) 
        mid.append(base[rem]) 
    return ''.join([str(x) for x in mid[::-1]]) 
    

def f6(s):
    return f3(f4(s.upper())) 

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

f = [None, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12]

def myprint(s):
    print s
    sys.stdout.flush()


def main():
    motd = \
    """
    ===================================================================
     ____            ______        ______            _
    / ___|  ___  ___|  _ \ \      / / ___| _   _ ___| |_ ___ _ __ ___
    \___ \ / _ \/ __| |_) \ \ /\ / /\___ \| | | / __| __/ _ \ '_ ` _ \\
     ___) |  __/ (__|  __/ \ V  V /  ___) | |_| \__ \ ||  __/ | | | | |
    |____/ \___|\___|_|     \_/\_/  |____/ \__, |___/\__\___|_| |_| |_|
                                           |___/
    ===================================================================
    """

    myprint(motd)
    myprint("Can your break my password?")

    pw1 = level1()
    pw2 = level2()
    pw3 = level3()

    myprint("WTF! You break all the password! The flag is :")
    myprint(pw3.format(pw2, pw1))

def level1():
    myprint("Welcome to Level 1 ... Try to break me!")

    ans = 471186387451848374701282213440713470402895200679708722960352108591145331
    your_ans = raw_input("Give me your answer: ").strip()

    i = len(your_ans) - 1
    while ans > 0:
        if not ans & 0xff == ord(your_ans[i]):
            print "Failed!"
            exit()
        ans = ans >> 8
        i -= 1
    return your_ans


def level2():
    myprint("yo! You passed Level 2, but I have another password. lol")
    myprint("It's a meaningful word.")
    
    ans = "111010110111010000000001000001110010010011111101111110010011011010010011000001100111100"
    your_ans = raw_input("Give me a serial (a-b-c-d): ").strip("")

    s = []
    for t in your_ans.split('-'):
        if int(t) < 1 or int(t) >= len(f):
            print "out of range"
            exit()
        
        if int(t) in s:
            print "duplicate!"
            exit()

        s.append(int(t))
    
    your_ans = raw_input("Give me your answer: ")
    print f[s[3]](f[s[2]](f[s[1]]((int(f[s[0]](ans)) / 0xddaa))))
    #if len(your_ans) > 10:
    #    print "My password is shorter. :p"
    #    exit()

    if f[s[3]](f[s[2]](f[s[1]]((int(f[s[0]](ans)) / 0xddaa)))) != your_ans:
        print "Failed!"
        exit()
    return your_ans

def level3():
    myprint("Well, here is the flag... Just kidding. There is one more challenge. XD")
    myprint("It's a meaningful sentence with prefix SDG{...}")

    ans = "AGZ0AQD3A2V3LwqvZmN3MQVjAmp2BGMwAzZlZQLkAmD3AQL1AzH2AQVjA2VmZGqxZwRlZGVkA2D3MN=="
    your_ans = raw_input("Give me a serial (a-b-c): ").strip("")

    s = []
    for t in your_ans.split('-'):
        if int(t) < 1 or int(t) >= len(f):
            print "out of range"
            exit()
        
        if int(t) in s:
            print "duplicate!"
            exit()
        
        s.append(int(t))
    
    your_ans = raw_input("Give me your answer: ")

    if "SDG" not in your_ans:
        print "It's not my password!"
        exit()

    if f[s[2]](f[s[1]](f[s[0]](ans))) != your_ans:
        print "Failed!"
        exit()
    return your_ans

if __name__ == '__main__':
    main()
