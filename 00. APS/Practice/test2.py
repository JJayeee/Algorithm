import sys
sys.stdin = open('input_2383.txt','r')

def find(dist1, dist2, p1, p2):
   global result
   k1, k2 = 0, 0
   dist1.sort()
   dist2.sort()
   max_t = 0
   while p1 != 0 or p2 != 0:
       max_t += 1
       if p1 != 0:
           for x in dist1:
               if x[0] == 0 and x[2] == 0 and x[3] == 1:
                   p1 -= 1
                   k1 -= 1
                   x[3] = 0
           for x in dist1:
               if x[1] == 1:
                   if x[0] != 0:
                       x[0] -= 1
                   elif x[0] == 0 and x[2] != 0 and k1 < 3 and x[3] == 0:
                       k1 += 1
                       x[3] = 1
                   if x[0] == 0 and x[2] != 0 and k1 <= 3 and x[3] == 1:
                       x[2] -= 1
       if p2 != 0:
           for x in dist2:
               if x[0] == 0 and x[2] == 0 and x[3] == 1:
                   p2 -= 1
                   k2 -= 1
                   x[3] = 0
           for x in dist2:
               if x[1] == 1:
                   if x[0] != 0:
                       x[0] -= 1
                   elif x[0] == 0 and x[2] != 0 and k2 < 3 and x[3] == 0:
                       k2 += 1
                       x[3] = 1
                   elif x[0] == 0 and x[2] != 0 and k2 <= 3 and x[3] == 1:
                       x[2] -= 1
   result = min(result, max_t)
   return

def chk(t):
   p1 = 0
   p2 = 0
   for i in range(p_num):
       if t[i] == 1:
           dist1[i][1] = 1
           dist1[i][2] = stairs[0][2]
           p1 += 1
       else:
           dist2[i][1] = 1
           dist2[i][2] = stairs[1][2]
           p2 += 1
   return find(dist1, dist2, p1, p2)

def powerset(k, n):
   global t
   if k == n:
       chk(t)
   else:
       for i in range(2):
           t[k] = i
           powerset(k+1, n)
   return

T = int(input())
for tc in range(T):
   n = int(input())
   pan = [list(map(int,input().split()))for _ in range(n)]
   stairs = []
   dist1 = []
   dist2 = []
   k = 0
   p_num = 0
   for i in range(n):
       for j in range(n):
           if pan[i][j] > 1:
               stair = pan[i][j]
               stairs.append([i,j,pan[i][j]])
   for i in range(n):
       for j in range(n):
           if pan[i][j] == 1:
               dist1.append([abs(i-stairs[0][0])+abs(j-stairs[0][1]),0,0,0])
               dist2.append([abs(i-stairs[1][0])+abs(j-stairs[1][1]),0,0,0])
               p_num += 1
   t = [0] * p_num
   result = 9999
   powerset(0, p_num)
   print(result)