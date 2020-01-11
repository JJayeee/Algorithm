n = int(input())
papers = [tuple(map(int, input().split())) for _ in range(n)]
papers.sort(reverse=True)

stack = []
for i in range(n):
    nx, ny = papers[i]
    if stack:
        kx, ky = stack[-1]
        if kx < nx or ky < ny:
            stack.pop()
            stack.append((nx, ny))