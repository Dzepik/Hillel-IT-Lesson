"""
 программа "Касир в кінотеватрі."
"""

age = int(input('Enter you age: '))
if age < 7:
    print('Де твої батьки?')
elif 7 < age < 16:
    print('Це фільм для дорослих!')
elif age > 65:
    print('Покажіть пенсійне посвідчення!')
elif age == 7 or age == 17 or age == 27 or age == 37 or age == 47 or age == 57 or age == 67 or age == 77 or age == 87 or age == 97:
    print('Вам сьогодні пощастить!')
else:
    print('А білетів вже немає!')





