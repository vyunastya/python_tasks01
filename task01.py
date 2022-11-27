#1 Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
number_of_day = int(input("Введите день недели "))
if number_of_day > 8 or number_of_day < 1:
    print("Введена некорректная цифра дня недели")
elif number_of_day == 7 or number_of_day == 6:
    print("Да")
else:
    print("Нет")