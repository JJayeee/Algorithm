#### 2056. 연월일 달력

```python
for i in range(int(input())):
    date = input()
    day = int(date[6:])
    month = int(date[4:6])
    year = int(date[:4])

    yes = f'#{i+1} {date[:4]}/{date[4:6]}/{date[6:]}'
    no = f'#{i+1} -1'

    if 0 < month < 13:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if 0 < day < 32:
                print(yes)
            else:
                print(no)
        elif month in [9, 11, 4, 6]:
            if 0 < day < 31:
                print(yes)
            else:
                print(no)
        elif month == 2:
            if 0 < day < 29:
                print(yes)
            else:
                print(no)
    else: print(no)

```



#### 2050. 알파벳을 숫자로 변환

```python
char = input()
for i in char:
    print(ord(i)-64, end=' ')
```



#### 1936. 1대 1 가위바위보

```python
# 가위 = '1'
# 바위 = '2'
# 보 = '3'

# 가위(1) 바위(2) = 바위(2)
# 바위(2) 보(3) = 보(3)
# 보(3) 가위(1) = 가위(1)

a = input().split(' ')
A = int(a[0])
B = int(a[1])

if A % 3 > B % 3:
    print('B')
else:
    print('A')
```

```bash
3 2
A
```





#### 2072. 홀수만 더하기

```python
def is_even(n):
    return n % 2

for i in range(int(input())): 
    a = input().split()
    tr = map(int, a)
    b = filter(is_even, tr)
    pls = 0
    for number in b:
        pls += number
    print(f'#{i+1} {pls}')
```

```bash
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1   

#1 200
#2 208
#3 121
```



#### 2071. 평균값 구하기

```python
for i in range(int(input())): 
    a = input().split()
    numbers = list(map(int, a))
    result = round(sum(numbers) / len(numbers))
   
    print(f'#{i+1} {result}')
```

```bash
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1   

#1 24
#2 29
#3 27
```







#### 2070. 큰 놈, 작은 놈, 같은 놈 + ??????

```python

for i in range(int(input())): 

    a = input().split()
    numbers = list(map(int, a))
    if numbers[0] > numbers[1]:
        result = '>'
    elif numbers[0] == numbers[1]:
        result = '='
    else:
        result = '<'

    print(f'#{i+1} {result}')
```



```python
for i in range(int(input())):
    a,b = map(int,input().split())
    print(f'#{i+1} {a>b and ">" or a<b and "<" or "="}')
```





#### 2063. 중간값 찾기

```python
howmany = int(input())
a = input().split()
numbers = list(sorted(map(int, a)))
center = int(howmany / 2)
print(numbers[center])
```

```bash
199
85 72 38 80 69 65 68 96 22 49 67 51 61 63 87 66 24 80 83 71 60 64 52 90 60 49 31 23 99 94 11 25 24 51 15 13 39 67 97 19 76 12 33 99 18 92 35 74 0 95 71 39 33 39 32 37 45 57 71 95 5 71 24 86 8 51 54 74 24 75 70 33 63 29 99 59 94 52 13 35 99 46 57 71 23 17 3 94 48 77 18 83 11 83 25 59 62 2 78 86 7 94 65 80 32 39 84 60 65 72 61 58 84 8 72 12 19 47 49 49 59 71 52 34 22 21 20 92 33 80 39 74 9 28 97 100 93 29 25 4 66 79 81 98 21 91 62 82 4 59 100 34 1 51 80 92 69 77 39 38 97 51 34 35 19 22 1 67 9 90 31 82 11 51 84 78 70 74 42 100 88 53 80 57 62 32 51 48 63 92 46 4 61 31 98 69 52 88 20

58
```

#### +++

```python
sorted를 먼저 하느냐, map을 먼저하느냐가 차이가 남!!
list의 index 주의하기. 0부터 시작하기 때문에 center에 +1을 하지 않아도 된다.
sorted에 list를 해주지 않아도 되는듯?
```



#### 2068. 최대수 구하기

```python
for i in range(int(input())):
    numbers = input().split()
    sorted_n = sorted(map(int, numbers))
    print(f'#{i+1} {sorted_n[-1]}')
```

```bash
3 
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1   

#1 99
#2 123
#3 76
```

#### +++

````python
위와 똑같은 실수 ㅠㅠ int 안 하면 map 했을 때 결과가 다름
& range 안 함 ㅜㅜㅜ
````

```bash
22 8 5 123 7 2 63 7 3 46
['123', '2', '22', '3', '46', '5', '63', '7', '7', '8']
#1 8

22 8 5 123 7 2 63 7 3 46
[2, 3, 5, 7, 7, 8, 22, 46, 63, 123]
#1 123
```







#### 1938. 아주 간단한 계산기

```python
a = map(int, input().split())
plus = a[0] + a[1]
minus = a[0] - a[1]
multi = a[0] * a[1]
divide = round(a[0] / a[1])
print(plus, minus, multi, divide, sep='\n')
```

```bash
8 3

11
5
24
2
```

#### +++

````python
sep랑 end의 차이 유념하기
````



#### 1933. 간단한 N의 약수

````python
n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')
````

```bash
10

1 2 5 10
```





#### 1024. [S/W 문제해결 기본] 최빈수 구하기

```python
for i in range(int(input())):
    times = input()
    test_list = input().split()
    test_set = set(test_list)

    count_dict = {}
    for i in test_set:
        count_dict[i] = test_list.count(i)

    sample = 0
    for k, v in count_dict.items():
        if v > sample:
            sample = v
            key = k
    print(f'#{times} {key}')
```





#### 1284. 수도 요금 경쟁

```python
for i in range(int(input())):
    tl = list(map(int, input().split()))
    p, q, r, s, w = tl[0], tl[1], tl[2], tl[3], tl[4]

    m_a = p * w

    if w <= r:
        m_b = q
    else:
        m_b = (w - r) * s + q

    if m_a > m_b:
        print(f'#{i} {m_a}')
    else:
        print(f'#{i} {m_b}')
```

#### ++++++

```python
n = int(input())
 
for i in range(1, n+1):
     
    p, q, r, s, w = map(int, input().split(" "))
    a = p * w
    b = q if w <= r else q + s * (w - r)
     
    print(f'#{i} {min(a, b)}')
```



```python
for i in range(int(input())):
    tl = list(map(int, input().split()))
    p, q, r, s, w = tl[0], tl[1], tl[2], tl[3], tl[4]

    m_a = p * w
    m_b = q if w <= r else (w - r) * s + q
    
    print(f'#{i+1} {min(m_a, m_b)}')
```







#### 1946. 간단한 압축 풀기

```python
for tc in range(1, int(input())+1):
    b = []
    for t in range(int(input())):
        a = input().split()
        b += [a[0]] * int(a[1])
    print('#%d' % (tc))
    for i in range(len(b)//10 + 1):
        print(''.join(b[i*10:i*10+10]))
```







#### 2001. 파리퇴치

```python
def iswall(x, y):
    if x < 0 or n-1 < x: return False
    if y < 0 or n-1 < y: return False
    else: return True


def kill(x, y):
    a = 0
    for i in range(x, x+m):
        for j in range(y, y+m):
            if iswall(i, j):
                a += paris[i][j]
    return a


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    paris = [list(map(int, input().split())) for i in range(n)]
    max_k = 0
    for x in range(len(paris)):
        for y in range(len(paris)):
            if max_k < kill(x, y):
                max_k = kill(x, y)

    print('#%d %d' % (tc, max_k))
```

