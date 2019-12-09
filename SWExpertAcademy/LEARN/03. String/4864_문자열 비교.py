def brute(ptn, txt):
    i, j = 0, 0
    a = len(ptn)
    b = len(txt)
    while i < a and j < b:
        if ptn[i] != txt[j]:
            j -= i
            i = -1
        j += 1
        i += 1
    return 1 if i == a else 0


for tc in range(1, int(input()) + 1):
    ptn = input()
    txt = input()
    print('#%d %d' % (tc, brute(ptn, txt)))