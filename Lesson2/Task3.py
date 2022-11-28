""" Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
 *Пример:*

    - Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
    Необходимо сложить все значения словаря и вывести  сумму на экран. """
n=int(input('Enter N = '))

n_list = {i:float((1+(1/i))**i) for i in range(1, n+1)} 
print(n_list)
result = round(sum(n_list.values()),2)
#result = sum(n_list[x] for x in n_list) 
print(result)

