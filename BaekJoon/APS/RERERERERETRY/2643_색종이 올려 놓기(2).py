n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]
# papers.sort(reverse=True)

test_index_papers = [[] for _ in range(n)]
for i in range(n):
    kx, ky = papers[i]
    k_cnt = 0
    for j in range(n):
        if i != j:
            nx, ny = papers[j]
            if kx >= nx and ky >= ny or kx >= ny and ky >= nx:
                k_cnt += 1

    test_index_papers[k_cnt].append((kx, ky))

print(test_index_papers)
# stack = []
test_cnt_papers = 0
for i in range(n-1, -1, -1):
    if test_index_papers[i]:
        kx, ky = test_index_papers[i][0]
        test_cnt_papers = len(test_index_papers[i])
        # stack.extend(test_index_papers[i])
        for j in range(i-1, -1, -1):
            # print(test_index_papers[j])
            # print(kx, ky)
            for nx, ny in test_index_papers[j]:
                if kx >= nx and ky >= ny or kx >= ny and ky >= nx:
                    kx, ky = nx, ny
                    test_cnt_papers += 1
                    # stack.append((nx, ny))
        break

# print(stack)
print(test_cnt_papers)



"""
7
1 2
8 7
20 10
20 20
15 12
12 14
11 12

8
1 2
8 7
20 10
20 20
20 20
15 12
12 14
11 12

3
100 1
2 2
2 2

3
2 2
2 2
2 2

5
2 1
1 1
1 1
1 99
1 7

7
2 1
1 1
1 1
1 99
1 7
2 3
1 3
"""