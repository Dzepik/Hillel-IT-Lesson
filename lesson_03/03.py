"""
Існує ліст з різними даними, наприклад
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який сформує новий list (наприклад lst2),
який би містив всі числові змінні (int, float), які є в lst1.
"""
import copy

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 = ([elem for elem in lst1 if isinstance(elem, (int, float))])
print(lst2)


