def myitoa(x):
    sr =''
    while True:
        r = x % 10
        sr = sr + chr(r + ord('0'))
        x //= 10
        if x == 0: break

    s = ''
    for i in range(len(sr) - 1, -1, -1):
        s = s + sr[i]

    return s


def bruteforce(tstr, pstr):
    pos = 0
    idx = 0
    cnt = 0

    while(pos < (len(tstr)-len(pstr)+1)):
        cnt += 1
        if tstr[pos] == pstr[idx] :
            idx += 1
            while idx < len(pstr) :
                cnt += 1
                if tstr[pos+idx] != pstr[idx] :
                    idx = 0
                    break
                else:
                    idx += 1

            if idx == len(pstr):
                print("%d times computations" % cnt, end=" ")
                return pos

        pos += 1

    print("%d times computations" % cnt, end=" ")
    return -1

def computejump(pattern, pi):

    L = len(pattern)
    for i in range(L-1):
        pi[ord(pattern[i])] = L-i-1


def bmoore(tstr, pstr):
    n = len(tstr)
    m = len(pstr)
    jump = [m for _ in range(128)]
    computejump(pstr, jump)

    i = 1
    cnt =0
    while i < (n - m + 1):
        j = m - 1
        k = i+ m -1
        cnt += 1

        while j>0 and pstr[j] == tstr[k] :
            j -= 1
            k -= 1
            cnt += 1

        if j == 0:
            print("%d times computations" % cnt, end=" ")
            return i

        i += jump[ord(tstr[i+m-1])]

    print("%d times computations" % cnt, end=" ")
    return -1


text = "a pattern matching algorithms"
pattern = "rithm"

print("Brute force algorithm : ", end = ' ')
print("%d th position" % bruteforce(text,pattern))
print("Boyer Moore algorithm : ", end = ' ')
print("%d th position" % bmoore(text,pattern))


str = input()
s=''

N = int(len(str))
for i in range(N):
    s += str[N-i-1]

print(s)
print(myitoa(1234))