def page(low, high, pa, count):
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        count += 1
        if pa == middle:
            return count
        elif pa < middle:
            return page(low, middle, pa, count)
        elif pa > middle:
            return page(middle, high, pa, count)


for tc in range(1, int(input())+1):
    p, pa, pb = map(int, input().split())
    a_count = page(1, p, pa, 0)
    b_count = page(1, p, pb, 0)
    if a_count == b_count:
        print('#%d 0' % (tc))
    else:
        if min(a_count, b_count) == a_count:
            result = 'A'
        elif min(a_count, b_count) == b_count:
            result = 'B'
        print('#%d %s' % (tc, result))
