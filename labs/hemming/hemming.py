#soruce = '10110001101010111'

def control_bits_create(source):
    sourcelist = list()
    for i in range(len(source)):
        sourcelist.append(int(source[i]))

    b = 0
    while 2 ** b <= len(source) + b:
        b += 1
    numbers_list = list()
    control_bits_list = list()
    if len(sourcelist) == 1:
        if sourcelist[0] == 1:
            for i in range(3):
                control_bits_list.append(1)
            return control_bits_list
        if sourcelist[0] == 0:
            for i in range(3):
                control_bits_list.append(0)
            return control_bits_list
    for i in range(len(source) + b + 1):
        numbers_list.append(i + 1)

    control_bits_list = list()

    j = 0
    for i in range(len(numbers_list)):
        if numbers_list[i] == 2 ** j:
            control_bits_list.append(0)
            i += 1
            j += 1
        else:
            control_bits_list.append(i + 1)

    i = 0
    k = 1
    while i < len(control_bits_list):
        if control_bits_list[i] != 0:
            control_bits_list[i] = k
            k += 1
        i += 1

    i = 0
    while i < len(control_bits_list):
        try:
            if control_bits_list[i] != 0:
                control_bits_list[i] = sourcelist[control_bits_list[i] - 1]
            i += 1
        except IndexError:
            control_bits_list = control_bits_list[0:len(control_bits_list) - 1]
            break

    matrix_control_bits = list()
    n = 0
    while n < b:
        stars_list = list()
        if 2 ** n > 3:
            for j in range(2 ** n - 1):
                stars_list.append(' ')
        else:
            for j in range(n):
                stars_list.append(' ')
        for i in range(2 ** n, len(control_bits_list)):
            for j in range(2 ** n):
                stars_list.append(1)
            for j in range(2 ** n):
                stars_list.append(' ')
            i += 2 ** n
        matrix_control_bits.append(stars_list)
        n += 1

    for i in range(len(matrix_control_bits)):
        matrix_control_bits[i] = matrix_control_bits[i][0:len(control_bits_list)]

    n = 0
    while n < len(matrix_control_bits):
        sum = 0
        pr = 1
        for i in range(len(control_bits_list)):
            try:
                pr = matrix_control_bits[n][i] * control_bits_list[i]
                sum += pr
            except TypeError:
                pr = 0
                sum += pr
        if sum % 2 != 0:
            control_bits_list[2 ** n - 1] = 1
        n += 1

    return control_bits_list


def serch_error(error):
    sum_list = list()
    stepen_list = list()
    index_error = 0
    b = 0
    while 2 ** b <= len(error) + b:
        b += 1

    matrix_control_bits = list()
    n = 0
    while n < b:
        stars_list = list()
        if 2 ** n > 3:
            for j in range(2 ** n - 1):
                stars_list.append(' ')
        else:
            for j in range(n):
                stars_list.append(' ')
        for i in range(2 ** n, len(error)):
            for j in range(2 ** n):
                stars_list.append(1)
            for j in range(2 ** n):
                stars_list.append(' ')
            i += 2 ** n
        matrix_control_bits.append(stars_list)
        n += 1
    for i in range(len(matrix_control_bits)):
        matrix_control_bits[i] = matrix_control_bits[i][0:len(error)]
    n = 0
    while n < len(matrix_control_bits):
        sum = 0
        pr = 1
        for i in range(len(error)):
            try:
                pr = matrix_control_bits[n][i] * error[i]
                sum += pr
            except TypeError:
                pr = 0
                sum += pr
        sum_list.append(f'Сумма произведение, контрольных битов: {sum}')
        if sum % 2 != 0:
            stepen_list.append(n)
            index_error += 2 ** n
        n += 1
    return index_error, sum_list, stepen_list


source = input('Введите последовательность:\n')
long_block = int(input('Введите длину блока: '))
n = 0
iter = 1

while n < len(source):
    control_bits_stroka = ''
    control_bits = control_bits_create(source[n:n + long_block])
    for i in range(len(control_bits)):
        control_bits[i] = str(control_bits[i]) + ' '
        control_bits_stroka += control_bits[i]
    n += long_block
    print(f'№{iter} блока: {control_bits_stroka}')
    iter += 1

error = input('Введите блок с ошибкой\n')
error1 = error.split(' ')


for i in range(len(error1)):
    error1[i] = int(error1[i])

index_error, sum_list, stepen_list = serch_error(error1)

for i in range(len(sum_list)):
    print(sum_list[i])

s = ''
for i in range(len(stepen_list)):
    s += f'2^{stepen_list[i]} + '
s = s + f'= {index_error}'

print(s)
print(f'Ошибка находится на {index_error} позиции')

probel = ''
for i in range(index_error - 1):
    probel += '  '

probel += '^'

print(error)
print(probel)