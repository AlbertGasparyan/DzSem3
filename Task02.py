from random import randint


enter = int(input('Введите длинну списка, в котором будут сгенерированны числа:'))

def get_array_random(num):
    lst = [randint(-10, 10) for i in range(enter)]
    print('Ваш список:',lst)
    return lst

arg= get_array_random(enter)

def product_num(x):
    mult_num=x[::len(x)-1]
    print(mult_num)

product_num(arg)