# def iswall(x, y): return x < n and y < n

def sol(kx, ky, kway):
    global way_cnt

    if kx == n-1 and ky == n-1:
        way_cnt += 1

    else:
        if kway == 0:
            if ky + 1 < n and arr[kx][ky+1] == 0:
                sol(kx, ky+1, 0)

        if kway == 1:
            if kx + 1 < n and arr[kx+1][ky] == 0:
                sol(kx+1, ky, 1)

        if kway == 2:
            if ky + 1 < n and arr[kx][ky+1] == 0:
                sol(kx, ky+1, 0)
            if kx + 1 < n and arr[kx+1][ky] == 0:
                sol(kx+1, ky, 1)

        if ky + 1 < n and kx + 1 < n and 0 == arr[kx+1][ky+1] == arr[kx][ky+1] == arr[kx+1][ky]:
            sol(kx+1, ky+1, 2)



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

way_cnt = 0
sol(0, 1, 0)
print(way_cnt)