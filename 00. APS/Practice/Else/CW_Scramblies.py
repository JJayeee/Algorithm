def scramble(s1, s2):
    chars = {chr(i):0 for i in range(97, 123)}
    for w in s1:
        chars[w] += 1
    for w in s2:
        if chars[w]:
            chars[w] -= 1
        else:
            return False
    return True

# Best Practices
def scramble2(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True
