from random import randint

N = int(input('Введите чило: '))
numbers = []
I = 0
while I < N:
    numbers.append(randint(-N,N))
    I+=1
print(f'Список случайных чисел ({-N}:{N}) = {numbers}')
position = []
for pos in range(0,2):
    position.append(int(input('Введите позицию чисел ')))
print(f'Выбраны числа на позициях {position}')
print(f'Произведение {numbers[position[0]-1]} и {numbers[position[1]-1]} равно {numbers[position[0]-1]*numbers[position[1]-1]}')
