import itertools

size = int(input('Введите размер списка: \n'))
work = list(range(1, size + 1))
result = list(itertools.permutations(work))
for element in result:
    print(element)
    
