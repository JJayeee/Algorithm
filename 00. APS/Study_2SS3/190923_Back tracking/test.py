# powerset(1) 연습

def powerset1(s):
    power_set = [[]]
    for elem in s:
        for sub_set in power_set:
            power_set = power_set + [list(sub_set) + [elem]]
            print(sub_set)
            print(power_set)
    return power_set

test = [1, 3, 4]
print(powerset1(test))
