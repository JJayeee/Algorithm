
def solution(k, score):
    length = len(score)
    hack = {}
    nums = {}

    for i in range(1, length):
        b = abs(score[i-1] - score[i])
        if hack.get(b):
            hack[b].append(i)
            nums[b] += 1
        else:
            hack[b] = [i]
            nums[b] = 1

    visited = [0]*length
    for key, val in nums.items():
        if val >= k:
            for v in hack[key]:
                if not visited[v]:
                    length -= 1
                    visited[v] = 1
                if not visited[v-1]:
                    visited[v-1] = 1
                    length -= 1

    return length


k, score = 3, [24,22,20,10,5,3,2,1]
# k, score = 2, [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]

print(solution(k, score))

