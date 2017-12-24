def draw_triangle(height, sym):
    for i in range(height + 1):
        print(i * sym)
    return


height = int(input('Введите высоту треугольника: \n'))
sym = input('Введите символ рисования треугольника: \n')

draw_triangle(height, sym)
