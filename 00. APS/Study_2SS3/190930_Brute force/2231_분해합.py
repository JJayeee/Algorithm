"""
216
-> 198
"""


n = input()
number = int(n)
min_n = int(n) - 9*(len(n))
min_n = 0 if min_n < 0 else min_n
result = 0
for tmp in range(min_n, number):
    temp = str(tmp)
    temp_sum = tmp
    for t in temp:
        temp_sum += int(t)
    if temp_sum == number:
        result = tmp
        break
print(result)
