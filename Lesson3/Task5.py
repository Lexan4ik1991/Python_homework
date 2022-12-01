""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,-13, -8, -5, −3, -2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] """

n=int(input('Введите число - '))
def fib(n):
 if n in [1,2]:
    return 1
 else:
    return fib(n-1)+fib(n-2)
print(f'Число Фибоначчи от {n} равно {fib(n)}')
m_list = []
n_list = []
for e in range (1,10):
    n_list.append(fib(abs(e))*-1)
    n_list.sort()
    m_list.append(fib(e))
    lst=n_list+m_list

print(lst)


