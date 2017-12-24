def result(name, age):
    if 1 < age < 10:
        print('У ' + name + ' детский возраст.')
    if 10 < age < 25:
        print('У ' + name + ' юный возраст.')
    if 25 < age < 44:
        print('У ' + name + ' молодой возраст.')
    if 44 < age < 60:
        print('У ' + name + ' средний возраст.')
    if 60 < age < 75:
        print('У ' + name + ' пожилой возраст.')
    if 75 < age < 90:
        print('У ' + name + ' старческий возраст.')
    if 90 < age:
        print(name + ' - долгожитель.')
    return


name = input('Введите Ваш имя: \n')
age = int(input('Введите Ваш возраст: \n'))

if 0 < age < 500:
    result(name, age)
