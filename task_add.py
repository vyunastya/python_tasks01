#5 Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве
# (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти расcтояние в 3D пространстве)
x_a = int(input("Введите координаты первой точки. X = "))
y_a = int(input("Y = "))
z_a = int(input("Z = "))
x_b = int(input("Введите координаты второй точки. X = "))
y_b = int(input("Y = "))
z_b = int(input("Z = "))
distance = ( (x_b - x_a) ** 2 + (y_b - y_a) ** 2 + (z_b - z_a) ** 2) ** 0.5
print(f'Расстояние между 2 точками в пространстве равно {distance:.{2}f}')