def sum_row(row):
    row_m = 0
    for i in range(len(row)):
        if row_m < sum(row[i]):
            row_m = sum(row[i])
    return row_m


def sum_column(row):
    coloum_m = 0
    for i in range(len(row)):
        coloum_sum = 0
        for j in range(len(row)):
            coloum_sum += row[j][i]
            if coloum_m < coloum_sum:
                coloum_m = coloum_sum
    return coloum_m


def sum_x(row):
    x_sum_0, x_sum_n = 0, 0
    for i in range(len(row)):
        x_sum_0 += row[i][i]
        x_sum_n += row[len(row)-1-i][len(row)-1-i]
    return max(x_sum_0, x_sum_n)


for tc in range(1):
    c_n = int(input())
    row = []
    for i in range(100):
        row.append(list(map(int, input().split())))


    print('#%d %d' % (c_n, max(sum_row(row), sum_column(row), sum_x(row))))

