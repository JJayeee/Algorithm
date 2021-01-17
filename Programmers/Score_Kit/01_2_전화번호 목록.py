def solution(phone_book):
    answer = True
    numbers_dict = {}

    for num in phone_book:
        pb = numbers_dict
        for n in num:
            pb.setdefault(n, {})
            pb = pb[n]
            if pb.get('fin'):
                answer = False
                break
        else:
            if pb.keys():
                answer = False
                break
            pb['fin'] = 1
        if not answer:
            break

    return answer


phone_book = ['119', '118', '19', '97674223', '1195524421']
phone_book = ['123', '12', '456', '789']
print(solution(phone_book))