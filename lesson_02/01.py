"""
 программа "Касир в кінотеватрі."
"""


while True:
    age = input('Enter you age, int: ')
    if age.isdigit():
        print(f'Thanks for {age}')
        break
    else:
        print(f'{age} - it is not int!')
age = int(age)

if age < 7:
    print('Де твої батьки?')
elif 7 < age < 16:
    print('Це фільм для дорослих!')
elif age > 65:
    print('Покажіть пенсійне посвідчення!')
elif '7' in str(age):
    print('Вам сьогодні пощастить!')
else:
    print('А білетів вже немає!')





