def str_to_int(string):
    string = string.split()
    my_list = []
    for element in string:
        if element != ' ':
            my_list.append(int(element))
    return my_list


def sum(str_to_int):
    even_sum = 0
    for element in str_to_int:
        if element % 2 != 0:
            even_sum = even_sum + element
    return even_sum


line = input('Введите строку последовательности: \n')

print(str_to_int(line))
print(sum(str_to_int(line)))
