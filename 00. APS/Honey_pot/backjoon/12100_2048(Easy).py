import collections

def move(karr, d):
    narr = [[0]*n for _ in range(n)]
    if d > 1:
        kd = d - 2
        karr = list(map(list, zip(*karr)))
    else:
        kd = d

    if kd == 0:
        for x_idx, garo in enumerate(karr):
            stack = collections.deque()
            y_idx = 0
            for y in range(n):
                if garo[y]:
                    if stack:
                        if stack[-1] == garo[y]:
                            k = stack.pop()
                            while stack:
                                narr[x_idx][y_idx] = stack.popleft()
                                y_idx += 1
                            narr[x_idx][y_idx] = k * 2
                            y_idx += 1
                        else:
                            stack.append(garo[y])
                    else:
                        stack.append(garo[y])
            while stack:
                narr[x_idx][y_idx] = stack.popleft()
                y_idx += 1

    else:
        for x_idx, garo in enumerate(karr):
            stack = collections.deque()
            y_idx = n-1
            for y in range(n-1, -1, -1):
                if garo[y]:
                    if stack:
                        if stack[-1] == garo[y]:
                            k = stack.pop()
                            while stack:
                                narr[x_idx][y_idx] = stack.popleft()
                                y_idx -= 1
                            narr[x_idx][y_idx] = k * 2
                            y_idx -= 1
                        else:
                            stack.append(garo[y])
                    else:
                        stack.append(garo[y])
            while stack:
                narr[x_idx][y_idx] = stack.popleft()
                y_idx -= 1

    if d > 1:
        karr = list(map(list, zip(*karr)))
        narr = list(map(list, zip(*narr)))

    return narr


def sol(depth, karr):
    global max_num
    if depth == 5:
        max_num = max(max_num, max(map(max, karr)))
        return
    else:
        for d in range(4):
            sol(depth+1, move(karr, d))


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# up, down, left, right
max_num = 0
sol(0, arr)
print(max_num)

# test = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# test = list(map(list, zip(*test)))
# print(test)
# test = list(map(list, zip(*test)))
# print(test)
