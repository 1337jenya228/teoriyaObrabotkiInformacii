def test_Pepin(number_Ferma):
    base = 3

    power = 2 ** number_Ferma - 1
    value_Ferma = 2 ** (2 ** number_Ferma) + 1

    for i in range(1, power+1):
        base = (base ** 2) % value_Ferma

    if base == (value_Ferma - 1):
        print ('Число F' + str(number_Ferma) + ' простое')
    else:
        print ('Число F' + str(number_Ferma) + ' составное')
    print('F' + str(number_Ferma) + ' = ' + str(value_Ferma))

test_Pepin(int(input('Введите номер числа Ферма: ')))