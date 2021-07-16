def solution(n, k, cmd):
    answer = ''
    visited = [[i-1, i, i+1] for i in range(n)]

    deleted_idx = []
    for w in cmd:
        f, i, r = visited[k]

        if w[0] == 'U':
            for _ in range(int(w[-1])):
                k = visited[k][0]

        elif w[0] == 'D':
            for _ in range(int(w[-1])):
                k = visited[k][2]

        elif w[0] == 'C':
            if f == -1:
                visited[i] = [0, i, 0]
                deleted_idx.append(i)
                visited[r][0] = -1
                k = r
            elif r == n:
                visited[i] = [0, i, 0]
                deleted_idx.append(i)
                visited[f][2] = n
                k = f
            else:
                visited[i] = [0, i, 0]
                deleted_idx.append(i)
                visited[f][2] = r
                visited[r][0] = f
                k = r

        else:
            alive_idx = deleted_idx.pop()
            f_idx, r_idx = alive_idx - 1, alive_idx + 1
            nf, nr = -1, n

            while n > f_idx > -1:
                if visited[f_idx][2]:
                    visited[f_idx][2] = alive_idx
                    nf = f_idx
                    break
                else:
                    f_idx -= 1

            while 0 <= r_idx < n:
                if visited[r_idx][0] or visited[r_idx][2]:
                    visited[r_idx][0] = alive_idx
                    nr = r_idx
                    break
                else:
                    r_idx += 1

            visited[alive_idx] = [nf, alive_idx, nr]


    for a, b, c in visited:
        if a or c:
            answer += 'O'
        else:
            answer += 'X'

    return answer


n = 8
k = 2
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))
