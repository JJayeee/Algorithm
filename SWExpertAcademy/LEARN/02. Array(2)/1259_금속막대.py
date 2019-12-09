for tc in range(1, int(input()) + 1):
    num = int(input())
    case = list(map(int, input().split()))
    nasa = {}
    for i in range(num):
        nasa[case[2 * i]] = case[2 * i + 1]

    max_link = []
    for key in nasa.keys():
        link = []
        while nasa.get(key):
            link.extend((key, nasa[key]))
            key = nasa[key]
        if len(link) > len(max_link):
            max_link = link
    result = ' '.join(map(str, max_link))
    print('#%d %s' % (tc, result))