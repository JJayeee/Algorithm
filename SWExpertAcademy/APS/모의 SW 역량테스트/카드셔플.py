# 캉
def card_shuffle(temp_list, mid, shuffle_cnt, shuffle_dial):
    temp_list1 = temp_list[:mid]  # 앞에 반
    temp_list2 = temp_list[mid:]  # 뒤에 반
    shuffle_list = []  # 내가 정렬해서 만들 리스트

    if mid > shuffle_dial:  # shuffle 번호 -> 1 ~ mid-1까지 구현
        for _ in range(mid - shuffle_dial):
            shuffle_list.append(temp_list1.pop(0))
        for _ in range(shuffle_dial):
            shuffle_list.append(temp_list2.pop(0))
            shuffle_list.append(temp_list1.pop(0))
        while temp_list2:
            shuffle_list.append(temp_list2.pop(0))
    else:  # 나머지 구현
        for _ in range(shuffle_dial - mid + 1):
            shuffle_list.append(temp_list2.pop(0))
        for _ in range(n - shuffle_dial - 1):
            shuffle_list.append(temp_list1.pop(0))
            shuffle_list.append(temp_list2.pop(0))
        while temp_list1:
            shuffle_list.append(temp_list1.pop(0))

    # 오름차순 내림차순 확인
    if shuffle_list == result_list1 or shuffle_list == result_list2:
        return shuffle_cnt
    else:
        if shuffle_cnt == 5:
            return 6
        else:
            cnt = 6
            # 1 ~ n-1 셔플
            for i in range(1, n):
                cnt = min(cnt, card_shuffle(shuffle_list, mid, shuffle_cnt + 1, i))
            return cnt


for tc in range(1, int(input().strip()) + 1):
    n = int(input().strip())  # 카드 수
    card_list = list(map(int, input().strip().split()))  # 카드 번호 리스트
    result_list1 = sorted(card_list)  # 오름차순
    result_list2 = list(reversed(result_list1))  # 내림차순
    shuffle_cnt = 6  # cnt 변수 선언 및 초기화 => 5초과 x

    # #오름차순 내림차순 확인 => 정렬할 필요 없는 경우
    if card_list == result_list1 or card_list == result_list2:
        shuffle_cnt = 0
    else:
        # 1 ~ n-1 셔플
        for i in range(1, n):
            shuffle_cnt = min(shuffle_cnt, card_shuffle(card_list, n // 2, 1, i))

    if shuffle_cnt == 6:
        print('#%d -1' % (tc))
    else:
        print('#%d %d' % (tc, shuffle_cnt))