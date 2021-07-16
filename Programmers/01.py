"""
어떤 메신저 회사에서는 해킹으로부터 고객들을 보호하기 위해,
신규 아이디의 password가 다음 규칙을 만족하도록 강제하고 있습니다.

1. 8 ≤ password 길이 ≤ 15

2. password는 아래 4 종류의 문자 그룹을 제외한,
    다른 어떤 문자도 포함해서는 안됩니다.
    [1] 알파벳 대문자(A~Z)
    [2] 알파벳 소문자(a~z)
    [3] 숫자(0~9)
    [4] 특수문자(~!@#$%^&*)

3. password는 (2.)에서 명시된 4 종류의 문자 그룹 중에서
    3 종류 이상을 포함해야 합니다.

4. password에 같은 문자가 4개 이상 연속될 수 없습니다.

5. password에 같은 문자가 5개 이상 포함될 수 없습니다.

고객들이 password로 사용하기 위해 입력한 문자열 inp_str가 매개변수로 주어집니다.
 이때, 위에서 나열한 규칙들 중 위배되는 규칙들의 번호를 배열에 담아 오름차순 정렬하여 return
 하도록 solution 함수를 완성해주세요. 만약 위배된 규칙이 하나도 없다면, 0을 담아서 return 합니다.

1 ≤ inp_str의 길이 ≤ 1,000,000
inp_str는 알파벳 대문자(A~Z), 알파벳 소문자(a~z), 숫자(0~9), 특수문자(~!@#$%^&*()-_=+)의 조합으로 구성되는 문자열입니다.
password로 허용되지 않는 특수문자(()-_=+)가 inp_str에는 나타날 수 있습니다.
"""


def get_flag3(n):
    global flag3_list
    global flag3_cnt

    if not flag3_list[n]:
        flag3_list[n] = 1
        flag3_cnt += 1


def solution(inp_str):
    global flag3_list
    global flag3_cnt

    answer = []
    flags = [0, 0, 0, 0, 0, 0]
    idx = 0
    flag4_pre = ''
    flag4_cnt = 0
    flag5_dict = {}

    if 8 > len(inp_str) or len(inp_str) > 15:
        flags[1] = 1
        flags[0] += 1

    while idx < len(inp_str):
        w = inp_str[idx]

        if w.isupper():
            get_flag3(0)

        elif w.islower():
            get_flag3(1)

        elif w.isdecimal():
            get_flag3(2)

        elif w in '~!@#$%^&*':
            get_flag3(3)

        else:
            flags[2] = 1
            flags[0] += 1

        if flag4_pre == w:
            flag4_cnt += 1
            if not flags[4] and flag4_cnt >= 4:
                flags[4] = 1
                flags[0] += 1
        else:
            flag4_cnt = 1

        if not flags[5]:
            flag5_dict[w] = flag5_dict.get(w, 0)
            flag5_dict[w] += 1
            if flag5_dict[w] >= 5:
                flags[5] = 1
                flags[0] += 1

        flag4_pre = w
        idx += 1

    if flag3_cnt < 3:
        flags[3] = 1
        flags[0] += 1

    if not flags[0]:
        return [0]
    else:
        for i in range(1, 6):
            if flags[i]:
                answer.append(i)
        return answer


flag3_list = [0, 0, 0, 0]
flag3_cnt = 0


# int_str = "AaTa+!12-3"
# int_str = "aaaaZZZZ)"
# int_str = "UUUUU"
# int_str = "CaCbCgCdC888834A"
int_str = "ZzZz9Z824"

print(solution(int_str))