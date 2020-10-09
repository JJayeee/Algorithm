
import datetime

def solution(n, customers):
    customer_info = []

    for customer in customers:
        d, t, w = customer.split()
        h, mm, s = map(int, t.split(':'))
        m, d = map(int, d.split('/'))
        start_date = datetime.datetime(year=2020, month=m, day=d, hour=h, minute=mm, second=s)
        work_time = datetime.timedelta(minutes=int(w))
        customer_info.append((start_date, work_time))

    how_hard_work = [0]*(n+1)

    d = datetime.datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
    kiosk_info = [(d, i) for i in range(1, n+1)]

    while customer_info:
        arrival, work = customer_info.pop(0)
        end_time, idx = kiosk_info.pop(0)

        how_hard_work[idx] += 1

        if arrival < end_time:
            kiosk_info.append((end_time + work, idx))
        else:
            kiosk_info.append((arrival + work, idx))
        kiosk_info.sort()

    return max(how_hard_work)



# n = 3
# customers = ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]
n = 2
customers = ["02/28 23:59:00 03","03/01 00:00:00 02", "03/01 00:05:00 01"]
print(solution(n, customers))
