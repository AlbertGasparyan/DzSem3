from random import randint


enter = int(input('Введите длинну списка, в котором будут сгенерированны числа:'))

def get_array_random(num):
    lst = [randint(-10, 10) for i in range(enter)]
    print('Ваш список:',lst)
    return lst

arg= get_array_random(enter)

def product_num(lst):
    l = len(lst) // 2 + 1 if len(lst) % 2 != 0 else len(lst) // 2
    new_lst = [lst[i] * lst[len(lst) - i - 1] for i in range(l)]
    print(f'Произведение крайних чисел массива: {new_lst}')

product_num(arg)