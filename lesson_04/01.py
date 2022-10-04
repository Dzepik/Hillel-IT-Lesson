"""
Дана довільна строка. Напишіть код, який знайде в ній і виведе на екран
кількість слів, які містять дві голосні літери підряд.
"""

my_string = input('Enter the text: ')
my_list = my_string.split()
count = 0
glas = 'AaEeIiOoUu'
for word in my_list:
    for i in range(len(word)-1):
        if word[i] in glas and word[i+1] in glas:
            count += 1
            continue
print(count)













