""" Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10 """



num = int(input('Enter num - '))
num2 =''
while num > 0:
    num2 = str(num % 2) + num2
    num = num // 2
print(num2)


""" num = int(input('Enter num - '))
num2= bin(num)
print(num2) """