s = ''
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while n != 0:
    s = str(n % 2) + s
    n //= 2
print(s)