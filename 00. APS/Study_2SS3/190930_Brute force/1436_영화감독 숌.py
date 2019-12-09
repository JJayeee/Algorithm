n = int(input())

cnt = 0
result = 665
while cnt != n:
    result += 1
    if '666' in str(result):
        cnt += 1

print(result)