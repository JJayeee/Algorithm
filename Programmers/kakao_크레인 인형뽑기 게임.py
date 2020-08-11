def solution(board, moves):
    answer = 0
    x, y = len(board), len(board[0])

    where_doll = [0] * y
    for ky in range(y):
        for kx in range(x):
            if board[kx][ky]:
                where_doll[ky] = kx
                break

    stack = []
    for m in moves:
        m -= 1
        if where_doll[m] < x:
            new_doll = board[where_doll[m]][m]
            where_doll[m] += 1
            if stack and stack[-1] == new_doll:
                stack.pop()
                answer += 1
            else:
                stack.append(new_doll)

    return answer


board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
