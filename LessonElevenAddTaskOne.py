import itertools

size = int(input('Введите размер списка: \n'))
work = []
for i in range(size):
    work.append(i + 1)
result = list(itertools.permutations(work))
for element in result:
    print(element)
