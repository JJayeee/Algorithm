def win(x, y):
    if (lst[x-1] == 1 and lst[y-1] == 3) or (lst[x-1] == 1 and lst[y-1] == 1):
        return x
    elif (lst[x-1] == 2 and lst[y-1] == 1) or (lst[x-1] == 2 and lst[y-1] == 2):
        return x
    elif (lst[x-1] == 3 and lst[y-1] == 2) or (lst[x-1] == 3 and lst[y-1] == 3):
        return x
    return y


def match(start, end):
    if start == end:
        return start

    v1 = match(start, (start+end)//2)
    v2 = match((start+end)//2+1, end)
    return win(v1, v2)


for tc in range(1, int(input())+1):
    n = int(input())
    lst = list(map(int, input().split()))
    start = 1
    end = n
    print('#%d %d' % (tc, match(start, end)))




#
# import sys
# sys.stdin=open("card_input.txt","r")

def find(l, r):
    if l==r:
        return l
    else:
        r1 = find(l, (l+r)//2)
        r2 = find((l+r)//2+1, r)
        if card[r1]==card[r2]:
            return r1
        else:
            if card[r1]==1 and card[r2]==2:             # 가위 vs 바위
                return r2
            elif card[r1]==1 and card[r2]==3:           # 가위 vs 보
                return r1
            elif card[r1]==2 and card[r2]==1:           # 바위 vs 가위
                return r1
            elif card[r1]==2 and card[r2]==3:           # 바위 vs 보
                return r2
            elif card[r1]==3 and card[r2]==1:           # 보 vs 가위
                return r2
            elif card[r1]==3 and card[r2]==2:           # 보 vs 바위
                return r1

def whoWin(st1,st2):

    if card[st1] == card[st2]:
        return st1

    # 1: 가위 2: 바위 3: 보
    if card[st1] == "1" and card[st2] =="2":    # 가위 vs 바위
        return st2
    elif card[st1] =="2" and card[st2] =="3":    # 바위 vs 보
        return st2
    elif card[st1] == "3" and card[st2] =="1":    # 보 vs 가위
        return st2

    return st1


def torGame(start, end):

    if start == end:
        return  start

    if start+1 == end:
        return whoWin(start,end)

    half = (start + end)//2
    win1 = torGame(start, half)
    win2 = torGame(half+1, end)
    return whoWin(win1, win2)


Tc = int(input())

for i in range(Tc):
    N = int(input())
    card = list(input().split())

    print("#%d" % (i+1),torGame(0,N-1)+1)

#    card = [0]+list(map(int, input().split()))           # 인덱스 1번부터 저장
#    print('#{} {}'.format(tc, find(1, N)))
