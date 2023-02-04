from random import randint

enter = int(input('Введите длинну списка, в котором будут сгенерированны числа:'))

def get_array_random(num):
    lst = [randint(-10, 10) for i in range(enter)]
    print('Ваш список:',lst)
    return lst

arg= get_array_random(enter)

def sum_index_numbers(list):
    sum=0
    for i in range(1,len(list),2):
        sum+=list[i]
    print(f'Сумма нечётных позиций списка = {sum}')

sum_index_numbers(arg)


