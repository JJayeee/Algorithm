def bin(i):
    global result
    for j in range(3, -1, -1):
        result += '1' if i & (1 << j) else '0'

for tc in range(1, int(input())+1):
    n, num = input().split()
    result = ''
    for i in range(int(n)):
        a = num[i]
        if a.isalpha():
            a = ord(a) - ord('A') + 10
            bin(a)
        else:
            bin(int(a))
    print('#%d %s' % (tc, result))


# int(str, 16) : 16진수로 바로 바꿈