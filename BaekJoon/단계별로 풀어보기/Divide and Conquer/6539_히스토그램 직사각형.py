"""
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
14 3 2 1 3 2 1 1 0 2 1 1 0 1 2
0

"""

while 1:
    tmp = input()
    if tmp == '0':
        break
    else:
        squares = [int(w) for w in tmp.split()]
        squares.append(-1)
        n = squares[0]
        stack = []
        max_wh = 0
        for i in range(1, n+2):
            if not stack:
                stack.append((i, squares[i]))
            else:
                if stack[-1][1] < squares[i]:
                    stack.append((i, squares[i]))
                elif stack[-1][1] > squares[i]:
                    tmp_idx = stack[-1][0]
                    while stack and stack[-1][1] > squares[i]:
                        idx, h = stack.pop()
                        tmp_idx = idx
                        k_wh = (i - idx) * h
                        if k_wh > max_wh:
                            max_wh = k_wh
                    stack.append((tmp_idx, squares[i]))
        print(max_wh)
