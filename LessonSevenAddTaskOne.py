string = str(input('Please enter the text for analysis: \n'))
my_list = list(string)

temp = []
count = 1
control = 1
while control == 1:
    for i in range(len(my_list)):
        if my_list[len(my_list)-1] == my_list[len(my_list)-2]:
            control = 0
        else:
            my_list = list(string)
            for j in range(0, len(my_list) // 2, count):
                temp.append(my_list[0:count + 1])
                del (my_list[0:count + 1])
            for k in range(len(temp)):
                my_list.append(temp[k])
            temp.clear()
            count += 1

for element in my_list[len(my_list)-1]:
    print(element, end='')
