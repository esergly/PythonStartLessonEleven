import random


# Вводим данные для расчёта максимальной суммы элементов с заданным направлением шага (вниз или вниз-вправо)
def manual_enter(size, gen):
    pyramid = []
    for i in range(size):
        for j in range(size):
            if gen == 1:
                n = (int(input('Введите значения ' + str(i) + ' строки ' + str(i + 1) + ': \n')))
                pyramid.append(n)
            if gen == 2:
                pyramid.append(random.randint(1, 100))
            if gen == 3:
                pyramid = [7, 5, 8, 9, 8, 2, 1, 3, 5, 6, 6, 2, 4, 4, 5, 9, 5, 3, 5, 5, 7, 7, 4, 6, 4, 7, 6, 8]
            if j == i:
                break
            else:
                j += 1
    return pyramid


def max_sum_line(manual_enter, size):
    temp = []
    if size == 0:
        print('Пирамида не создана!')
    if size != 0:
        print('\n\n Рассматриваемая пирамида: ')
        # Создание красивого вывода пирамиды
        while size != 0:
            temp.append(manual_enter[(len(manual_enter) - size):(len(manual_enter))])
            for i in range(size):
                manual_enter.pop()
            size -= 1
        temp.reverse()
        for element in temp:
            print(element)
        print('\n Максимальная сумма цепочки элементов: ')
    # Ядро расчёта
    z = []
    s = []

    # start
    x = temp[len(temp) - 1]
    y = temp[len(temp) - 2]
    for i in range(len(y)):
        z.append(y[i] + x[i])
        z.append(y[i] + x[i + 1])
        s.append(z[::])
        z.clear()
    del temp[- 2:]
    y.clear()

    x = temp[len(temp) - 1]

    for j in range(len(temp)):
        s[j] = s[j] + s[j + 1]

    del s[- 1:]
    for res in range(len(temp)):
        for k in range(len(temp)):
            n = 0
            while n < len(s[k]):
                z.append(s[k][n] + x[k])
                n += 1
            y.append(z[::])
            z.clear()
        s.clear()
        for l in range(len(y) - 1):
            s.append(y[l] + y[l + 1])
        if len(y) > 1:
            y.clear()
            del temp[len(temp) - 1:]
            x = temp[len(temp) - 1]

    return print(max(y[0]))


# Создаём что-то типа меню с выбором опций: создание горки сокровищ автоматически, с ручным указанием значений или с данными из условия
size = 0
gen = int(input(
    '\n1) Ручной ввод значений \n2) Автоматический ввод значений \n3) Ввод заданных значений \n\nВведите выбранный номер пункта из предложенных: \n '))
if gen == 1 or gen == 2:
    size = int(input('Введите размер пирамиды: \n'))
if gen == 3:
    size = 7
if gen < 1 or gen > 3:
    print('Введённый номер не корректен.')

max_sum_line(manual_enter(size, gen), size)
