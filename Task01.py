# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.


list1 = list()
import random
n = int(input('Введите n: '))
for i in range(1,n+1):
    list1.append(random.randint(0, 1))
print(list1)

key=0
for i in list1:
    if i == 1: 
        key +=1
    
print(min(key, n-key))
