def trotter(n):
    check = [0]*10
    b = 1
    while 0 in check:
        m = b * n
        a = list(map(int, str(m)))
        for i in range(len(a)):
            check[a[i]] += 1
        b += 1
        if b >= 100:  # n == 0 인 경우라고 함
            return "INSOMNIA"
    return m