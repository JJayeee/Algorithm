def Bbit_print(i):
    global output
    for j in range(3, -1, -1):
        output += '1' if i & (1 << j) else '0'

a = '01D06079861D79F99F'
output = ''
b = []
for t in a:
    if t == 'A':
        t = 10
    elif t == 'B':
        t = 11
    elif t == 'C':
        t = 12
    elif t == 'D':
        t = 13
    elif t == 'E':
        t = 14
    elif t == 'F':
        t = 15
    else:
        t = int(t)
    Bbit_print(t)


for i in range(0, len(output), 7):
    test = output[i:i+7]
    print()
    print('bit =', test)
    result = 0
    for j in range(len(test)):
        result += int(test[len(test)-1-j]) * 2**j

    print('result =', result)





#
def Bbit_print2(i):
    global bit_num
    output = ''
    for j in range(3, -1, -1):
        output += '1' if i & (1 << j) else '0'
    bit_num.append(output)

bit_num = []
for i in range(0, 16):
    Bbit_print2(i)

# ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']


a = '01D06079861D79F99F'
bit_str = ''
for t in a:
    if t.isalpha():
        tt = ord(t) - ord('A') + 10
        bit_str += bit_num[tt]
    else:
        bit_str += bit_num[int(t)]

# 000000011101000001100000011110011000011000011101011110011111100110011111



# 3
a = '0269FAC9A0'
pattern = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']
bit_maker = ''
for i in a:
    if i.isalpha():
        aa = ord(i) - ord('A') + 10
        bit_maker += bit_num[aa]
    else:
        bit_maker += bit_num[int(i)]

print(bit_maker)
lenth = len(bit_maker)
while lenth > 1:
    lenth -= 1
    if bit_maker[lenth] == '1':
        print()
        print(pattern.index(bit_maker[lenth-5:lenth+1]))
        print(bit_maker[lenth-5:lenth+1])
        lenth -= 5

