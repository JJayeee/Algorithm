def solution(play_time, adv_time, logs):
    answer = ''
    p = list(map(int, play_time.split(':')))
    play = p[0] * 60 * 60 + p[1] * 60 + p[2]

    time = [0]*(play+1)

    for l in logs:
        start, end = l.split('-')
        s = list(map(int, start.split(':')))
        s = s[0] * 60 * 60 + s[1] * 60 + s[2]
        e = list(map(int, end.split(':')))
        e = e[0] * 60 * 60 + e[1] * 60 + e[2]
        # print(s, e)
        for i in range(s, e + 1):
            time[i] += 1

    a = list(map(int, adv_time.split(':')))
    adv = a[0] * 60 * 60 + a[1] * 60 + a[2]
    # print(time)
    max_adv = sum(time[:adv+1])
    tmp_adv = max_adv
    start = 0
    for i in range(1, play-adv):
        s, e = time[i-1], time[i+adv+1]
        # print('idx', i, i+adv)
        # print(s, e)
        tmp_adv = tmp_adv - s + e
        # max_adv = max(max_adv, tmp_adv)
        if max_adv < tmp_adv:
            max_adv = tmp_adv
            start = i
            # print(tmp_adv)

    # print(start)
    # start = max_adv
    # print(start)
    h = (start) // 3600
    m = (start - h * 3600) // 60
    s = (start - h * 3600 - m * 60)
    # print(h, ':', m, ':', s)
    h = str(h)
    if len(h) == 1:
        h = '0' + h
    m = str(m)
    if len(m) == 1:
        m = '0' + m
    s = str(s)
    if len(s) == 1:
        s = '0' + s
    answer = h + ':' + m + ':' + s



    return answer


p = "02:03:55"
a = "00:14:15"
l = ["01:20:15-01:45:14",
     "00:40:31-01:00:00",
     "00:25:50-00:48:29",
     "01:30:59-01:53:29",
     "01:37:44-02:02:30"]
#
p = "99:59:59"
a = "25:00:00"
l = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
# p = '0:0:10'
# a = "0:0:3"
# l = ['0:0:1-0:0:2', '0:0:2-0:0:6']
print(solution(p, a, l))
