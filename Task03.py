# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.


n = int(input('Введите n: '))
key = True
i = 2
while key:
    if n % i == 0:
        print(i)
        key = False
    i += 1
