#2 Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in False, True:
    for y in False, True:
        for z in False, True:
            condition1 = not (x or y or z)
            condition2 = not x and not y and not z
            if condition1 == condition2:
                print(f'При X = {x}, Y = {y}, Z = {z}, логическое значение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно')
            else:
                print(f'При X = {x}, Y = {y}, Z = {z}, логическое значение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ложно')