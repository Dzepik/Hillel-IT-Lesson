"""
Зформуйте строку, яка містить певну інформацію про символ по його індексу
в відомому слові.
Наприклад "The [індекс символу] symbol in [тут слово]
is '[символ з відповідним порядковим номером]'".
Слово та номер отримайте за допомогою input() або скористайтеся константою.
Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".
"""


word = input('Enter a word: ')
index = int(input('Enter number letter: '))
result = word[int(index-1)]
print(f'The {index} symbol in {word} is {result}')



