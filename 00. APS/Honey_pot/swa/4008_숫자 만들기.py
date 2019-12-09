def calculate(a, b, c):
    if c < 2:
        if c == 0: return a + b
        else: return a - b
    else:
        if c == 2: return a * b
        else: return int(a / b)

def sol(knum, depth):
    global max_num, min_num
    if depth == n:
        max_num = max(max_num, knum)
        min_num = min(min_num, knum)

    else:
        for i in range(4):
            if calc[i] > 0:
                calc[i] -= 1
                temp = calculate(knum, nums[depth], i)
                sol(temp, depth+1)
                calc[i] += 1


for tc in range(1, int(input())+1):
    n = int(input())
    calc = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    max_num, min_num = -1000000001, 1000000001
    sol(nums[0], 1)
    print('#%d %d' % (tc, max_num - min_num))

"""
10
5
2 1 0 1
3 5 3 7 9
6
4 1 0 0
1 2 3 4 5 6
5
1 1 1 1
9 9 9 9 9
6
1 4 0 0
1 2 3 4 5 6
4
0 2 1 0
1 9 8 6
6
2 1 1 1
7 4 4 1 9 3
7
1 4 1 0
2 1 6 7 6 5 8
8
1 1 3 2
9 2 5 3 4 9 5 6
10
1 1 5 2
8 5 6 8 9 2 6 4 3 2
12
2 1 6 2
2 3 7 9 4 5 1 9 2 5 6 4
"""