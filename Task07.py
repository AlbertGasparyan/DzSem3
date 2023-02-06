length = int(input('Len arry'))
lst = list(map(int, input('num list').split()))
shift = int(input('shift num'))

lst = lst[-shift:] + lst[:-shift]

print(lst)