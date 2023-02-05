from random import randint


enter_user = int(input('Для создания списка из вещественных чисел введите его размерность:'))


def get_list(l):
    lst = [(randint(0,100)/10) for el in range(enter_user)]
    print(f'Ваш сгенерированный список: {lst}')
    return lst

arg = get_list(enter_user)


def max_min_value(arg):
    mv1=max(arg)
    mv2=min(arg)
    print(f'Максимальное и минимальное значение списка - {mv1} и {mv2}')
    sv= mv1-mv2//1
    print(f'Разница междумаксимальным и минимальным значением = {sv}')
    return sv
max_min_value(arg)