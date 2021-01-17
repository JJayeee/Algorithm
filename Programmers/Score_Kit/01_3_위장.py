
def solution(clothes):
    answer = 1
    closet = {}
    for cloth in clothes:
        closet[cloth[1]] = closet.get(cloth[1], 0) + 1

    for k, v in closet.items():
        answer *= v + 1

    return answer - 1


clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(clothes))
