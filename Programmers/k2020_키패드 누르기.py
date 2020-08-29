

def solution(numbers, hand):
    key_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    answer = ''
    hand_flag = 1 if hand == 'right' else 0

    left_now = key_dict['*']
    right_now = key_dict['#']
    for num in numbers:
        if num:
            if num % 3 == 1:
                left_now = key_dict[num]
                answer += 'L'
                continue
            elif not num % 3:
                right_now = key_dict[num]
                answer += 'R'
                continue

        kx, ky = key_dict[num]
        (lx, ly), (rx, ry) = left_now, right_now
        l_dist = abs(lx - kx) + abs(ly - ky)
        r_dist = abs(rx - kx) + abs(ry - ky)

        if l_dist < r_dist:
            flag = False
        elif l_dist > r_dist:
            flag = True
        else:
            flag = hand_flag

        if flag:
            right_now = (kx, ky)
            answer += 'R'
        else:
            left_now = (kx, ky)
            answer += 'L'

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
print(solution(numbers, 'right'))


"""
테스트 1 〉	통과 (0.04ms, 10.7MB)
테스트 2 〉	통과 (0.04ms, 10.8MB)
테스트 3 〉	통과 (0.07ms, 10.8MB)
테스트 4 〉	통과 (0.04ms, 10.9MB)
테스트 5 〉	통과 (0.04ms, 10.7MB)
테스트 6 〉	통과 (0.04ms, 10.8MB)
테스트 7 〉	통과 (0.04ms, 10.8MB)
테스트 8 〉	통과 (0.05ms, 10.8MB)
테스트 9 〉	통과 (0.05ms, 10.7MB)
테스트 10 〉	통과 (0.04ms, 10.8MB)
테스트 11 〉	통과 (0.06ms, 10.8MB)
테스트 12 〉	통과 (0.06ms, 10.8MB)
테스트 13 〉	통과 (0.07ms, 10.8MB)
테스트 14 〉	통과 (0.10ms, 10.7MB)
테스트 15 〉	통과 (0.19ms, 10.8MB)
테스트 16 〉	통과 (0.18ms, 10.8MB)
테스트 17 〉	통과 (0.35ms, 10.8MB)
테스트 18 〉	통과 (0.33ms, 10.9MB)
테스트 19 〉	통과 (0.37ms, 10.8MB)
테스트 20 〉	통과 (0.34ms, 10.8MB)
"""