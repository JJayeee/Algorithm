for tc in range(1, int(input()) + 1):
    opt = list(map(int, input().split()))
    lines = list(map(int, input().split()))

    zero = [0] * opt[1]
    for i in range(opt[2]):
        zero[lines[i]] += 1

    i = opt[0]
    count = 0
    check = 0
    while i < opt[1]:
        if check == opt[1]:
            count = 0
            break
        if zero[i] == 1:
            count += 1
            i += opt[0]
        else:
            i -= 1
            check += 1

    print('#%d %d' % (tc, count))



# 1
def find1(v, k, n, m):
    stations = [0] * (N + 1)
    for i in range(M):
        stations[v[i]] = 1

    cnt = cur = 0
    while( True ):
        pre = cur
        cur += K
        if cur >= N:
            break
        if stations[cur] == 1:
            cnt += 1
        else:
            for i in range(1, K + 1):
                if stations[cur - i] == 1:
                    cur -= i
                    cnt += 1
                    break
            if cur == pre:
                cnt = 0
                break

    return cnt

def find(v, k, n, m):
    v.insert(0, 0)              # 출발점과 종점 번호 추가
    v.append(n)
    last = 0                    # 마지막 충전기
    cnt = 0                     # 충전 횟수
    for i in range(1, m+2):
        if (v[i]-v[i-1]) > k:   # 충전기 사이가  K보다 멀때
            return 0
        if v[i] > last + k:     # i충전기까지 갈 수 없으면
            last = v[i-1]       # 이전 충전기에서 충전
            cnt = cnt + 1
    return cnt

T = int(input())
for i in range(1,T+1):
    K, N, M = map(int, input().split())
    V = list(map(int, input().split()))
    print("#%d" % i, find1(V, K, N, M))


# 2
K, N, M = map(int, input().split())
stops = [0] + list(map(int, input().split())) + [N]

last = 0
cnt = 0
next = last + K

for i in range(1, M + 2):
    if (stops[i] - stops[i - 1]) > k:
        cnt = 0
        break

    if stops[i] > next:
        last = stops[i - 1]
        cnt += 1
        next = last + k