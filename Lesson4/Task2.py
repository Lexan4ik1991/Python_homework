""" Задайте натуральное число N. Напишите программу, 
которая составит список простых множителей числа N. """

num = int(input("Введите число: "))
lst = []
div = 2 
res = num
while num >= div:
    if num % div == 0:
        lst.append(div)
        num //= div
        div = 2
    else:
        div += 1
print(f"Простые множители приведены в списке: {lst}")
