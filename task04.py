#4 Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

axis = int(input("Введите номер четверти координат "))
if axis > 4 or axis < 1:
    print ("Некорректный номер четверти")
elif axis == 1:
    print("x > 0, y > 0 ")
elif axis == 2:
    print("x < 0, y > 0 ")
elif axis == 3:
    print("x < 0, y < 0 ")
else:
    print("x > 0, y < 0 ")