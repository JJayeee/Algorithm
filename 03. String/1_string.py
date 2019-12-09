a = 'reverse this strings'
print(a[::-1])

b = [i for i in a]
b.reverse()
print(''.join(b))

c = ''
for i in range(len(a)-1, -1, -1):
    c += a[i]
print(c)


def itoa(num):
    s = []
    while num > 0:
        s.append(num%10)
        num = num//10
    result = [chr(i+ord('0')) for i in s[::-1]]
    return ''.join(result)

num = 989670
print(itoa(num), type(itoa(num)))


t = 'this is a book'
p = 'is'
m = len(p)
n = len(t)

def bruteforce(p, t):
    i = 0
    j = 0
    while j < m and i < n:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == m:
        return i - m
    else:
        return -1

print(bruteforce(p, t))



test = 'a pattern matching algorithm'
pattern = 'it'

def brute(p, t):
    m = len(test)
    n = len(pattern)
    i = 0
    j = 0
    while i < m and j < n:
        if test[i] != pattern[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == n:
        return test[i - n], test[i - n + 1]
    else:
        return -1
print(brute(test, pattern))

