

def solution(companies, applicants):
    answer = []

    companies_dict = {}
    companies_get = {}
    companies_need = {}
    for idx, com in enumerate(companies):
        a, b, c = com.split()
        tmp_len = len(b)
        companies_dict[a] = {}
        for i in range(tmp_len):
            companies_dict[a][b[i]] = tmp_len - i
        companies_get[a] = []
        companies_need[a] = int(c)

    # print(companies_dict)
    # print(companies_get)

    applicants_dict = {}
    applicants_try = {}
    applicants_am_i = {}
    for app in applicants:
        a, b, c = app.split()
        applicants_dict[a] = [w for w in b]
        applicants_try[a] = [int(c), 0]
        applicants_am_i[a] = 0

    for i in range(4):
        apply_info = {k: [] for k in companies_dict.keys()}
        for k, v in applicants_try.items():

            if not applicants_am_i[k] and v[1] != v[0]:
                com_ = applicants_dict[k][v[1]]
                p = companies_dict[com_][k]
                apply_info[com_].append((p, k))
                v[1] += 1

        for key, val in apply_info.items():
            already_get = companies_get[key]
            # print(val)
            val = val + already_get
            val.sort(reverse=True)
            companies_get[key], left = val[:companies_need[key]], val[companies_need[key]:]

            for p, v in companies_get[key]:
                applicants_am_i[v] = 1

            for p, v in left:
                applicants_am_i[v] = 0


        # print(apply_info)
        # print(applicants_try)

    print(companies_get)
    for k, v in companies_get.items():
        tmp = []
        for p, vv in v:
            tmp.append(vv)
        tmp.sort()
        tt = ''
        for t in tmp:
            tt += t
        tmpp = k + '_' + tt
        answer.append(tmpp)

    return answer



companies = ["A fabdec 2", "B cebdfa 2", "C ecfadb 2"]
applicants = ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]
print(solution(companies, applicants))
