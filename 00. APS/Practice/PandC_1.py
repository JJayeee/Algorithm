def perm_i():
    for i1 in range(1, 4):
        for i2 in range(1, 4):
            if i2 != i1:
                for i3 in range(1, 4):
                    if i3 != i1 and i3 != i2:
                        print(i1, i2, i3)

def perm_r_3(k):
    if k == R:
        print(arr[0], arr[1], arr[2])
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm_r_3(k + 1)
            arr[k], arr[i] = arr[i], arr[k]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

N = 3
R = 3
t = [0] * N

print('순열 반복문')
perm_i()

print('순열 재귀문3')
perm_r_3(0)



def power_set_i():
    bit = [0, 0, 0]
    for i in range(2):
        bit[0] = i
        for j in range(2):
            bit[1] = j
            for k in range(2):
                bit[2] = k
                print(bit)


def power_set_b():
    arr = [1, 2, 3]
    n = len(arr)
    for i in range(1 << n):
        print('{', end =' ')
        for j in range(n+1):
            if i & (1 << j):
                print(arr[j], end = ' ')
        print('}')


print('부분집합 반복문')
power_set_i()

print('부분집합 바이너리 카운팅')
power_set_b()



def powersetlist(s):
    r = [[]]
    for e in s:
        temp= [x+[e] for x in r]
        r += temp
    return r


def powerset2(seq):
    #Returns all the subsets of this set. This is a generator.
    if len(seq) <= 1:
        #return [[], seq]
        yield seq
        yield []
    else:
        res =[]
        for item in powerset2(seq[1:]):
            #res.append(item)
            #res.append([seq[0]]+item)
            yield [seq[0]]+item
            yield item
        #return res


import time
tSet = [_ for _ in range(1, 21)]


stime = time.time()
s=0
for s1 in powersetlist(tSet):
   s += sum(s1)
print("powersetlist : ",s, end=" ")
etime = time.time()
print(etime-stime)


stime = time.time()
s = 0
for set1 in powerset2(tSet):
    # print(set1)
    s += sum(set1)
print("powerset2 : ",s, end=" ")
etime = time.time()
print(etime-stime)



