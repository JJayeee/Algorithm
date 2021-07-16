
def solution(s):
    answer = ''

    num_dict = {
        'ze': ['0', 4],
        'on': ['1', 3],
        'tw': ['2', 3],
        'th': ['3', 5],
        'fo': ['4', 4],
        'fi': ['5', 4],
        'si': ['6', 3],
        'se': ['7', 5],
        'ei': ['8', 5],
        'ni': ['9', 4],
    }

    idx = 0
    while idx < len(s):
        if ord('0') <= ord(s[idx]) <= ord('9'):
            answer += s[idx]
            idx += 1
            continue

        answer += num_dict[s[idx:idx + 2]][0]
        idx += num_dict[s[idx:idx + 2]][1]

    return int(answer)