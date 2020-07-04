# CH(CO2H)(CO2H)(CO2H)
# CH(CO2H)3

def get_sum(idx, k_sum):
    global result

    while idx < len(words):
        w = words[idx]
        if dict.get(w):
            try:
                k_sum += dict[w] * int(words[idx+1])
                idx += 2
            except ValueError:
                k_sum += dict[w]
                idx += 1
            except IndexError:
                k_sum += dict[w]
                idx += 1

        elif w == ')':
            return idx, k_sum

        elif w == '(':
            n_idx, n_sum = get_sum(idx + 1, 0)
            idx = n_idx + 1
            try:
                k_sum += n_sum * int(words[n_idx + 1])
                idx += 1
            except ValueError:
                k_sum += n_sum
            except IndexError:
                k_sum += n_sum

    result += k_sum
    return


dict = {'H': 1, 'C': 12, 'O': 16}
words = input()
result = 0
get_sum(0, 0)
print(result)
