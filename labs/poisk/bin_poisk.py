def binary_search(lst, search_item):
    low = 0
    high = len(lst) - 1
    search_res = False
    print('Начальный массив')
    for elemenet in range(len(lst)):
        print(lst[elemenet], ' ', end='')
    print()
    while low <= high and not search_res:
        middle = (low + high) // 2
        middle_element = lst[middle]
        if middle_element == search_item:
            search_res = True
            print('Средний элемент массива равен искомому числу')
            break
        if middle_element > search_item:
            high = middle - 1
            print('Средний элемент массива больше искомого числа')
            for elemenet in range(low,middle):
                print(lst[elemenet], ' ', end='')
            print()
        else:
            low = middle + 1
            print('Средний элемент массива меньше искомого числа')
            for elemenet in range(middle+1,high):
                print(lst[elemenet],' ', end = '')
            print()
    return search_res


lst = [61, 87, 154, 170, 275, 426, 503, 509, 512, 612, 653, 677, 703, 765, 897, 908]
value = int(input('Введите искомое число: '))
result = binary_search(lst, value)
if result:
    print("Элемент найден!")
else:
    print("Элемент не найден.")


