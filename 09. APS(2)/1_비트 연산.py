# 1
def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1<<j) else '0'
    print(output)

for i in range(-7, 6):
    print('%3d = ' % i, end='')
    Bbit_print(i)



# 2
a = '0000000111100000011000000111100110000110000111100111100111111001100111'
for i in range(0, len(a), 7):
    print()
    test = a[i:i+7]
    result = 0
    for j in range(0, 7):
        result += int(test[6-j]) * 2**j
    print('result =',  result)
    print('bit =', bin(result))
    print('original =', test)



# 3
n = 0x00111111

if n & 0xff:
    print('little endian')
else:
    print('big endian')



# 4
def ce(n):  # change endian
    p = []
    for i in range(0, 4):
        p.append((n >> (24 - i*8)) & 0xff)
    print(p)
    return p

def ce1(n):
    return (n << 24 & 0xff000000) | (n << 8 & 0xff0000) | (n >> 8 & 0xff00) | (n >> 24 & 0xff)

x = 0x01020304
p = []
for i in range(0, 4):
    p.append((x >> (i*8)) & 0xff)

print('x = %d%d%d%d' % (p[0], p[1], p[2], p[3]))
p = ce(x)
print('x = %d%d%d%d' % (p[0], p[1], p[2], p[3]))
print(ce1(n))



# 5
def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output)

a = 0x86
key  = 0xAA

print('a      ==> ', end='')
Bbit_print(a)

print('a^=key ==> ', end='')
a ^= key
Bbit_print(a)

print('a^=key ==> ', end='')
a ^= key
Bbit_print(a)
