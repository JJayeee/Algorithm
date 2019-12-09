for tc in range(1, int(input())+1):
    n, target = map(int, input().split())
    score = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        score.append((a*35 + b*45 + c*20) / n)

    toABC = sorted(score, reverse=True)
    grade = toABC.index(score[target-1])
    if 0 <= grade < n//10:
        result = 'A+'
    elif n//10 <= grade < n//10 * 2:
        result = 'A0'
    elif n//10 * 2 <= grade < n//10 * 3:
        result = 'A-'
    elif n//10 * 3 <= grade < n//10 * 4:
        result = 'B+'
    elif n//10 * 4 <= grade < n//10 * 5:
        result = 'B0'
    elif n//10 * 5 <= grade < n//10 * 6:
        result = 'B-'
    elif n//10 * 6 <= grade < n//10 * 7:
        result = 'C+'
    elif n//10 * 7 <= grade < n//10 * 8:
        result = 'C0'
    elif n//10 * 8 <= grade < n//10 * 9:
        result = 'C-'
    elif n//10 * 9 <= grade < n//10 * 10:
        result = 'D0'

    print('#%d %s' % (tc, result))
