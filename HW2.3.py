n = int(input())
list = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Последовательность: {list}\nСумма: {round(sum(list), 3)}')
