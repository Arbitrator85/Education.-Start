my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def f(my_list):
    if my_list[-1] == len(my_list)-1:
        res = str(my_list).strip('[]')
        return res + ' Конец списка'
    else:
        return f(my_list)

print(f(my_list))