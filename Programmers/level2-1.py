def solution(phone_book):
    number = {}
    phone = sorted(phone_book, key=lambda x: len(x))
    for ph in phone:
        number[ph] = 1
        for i in range(len(ph)):
            ph = ph[:-1]
            if number.get(ph):
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))

