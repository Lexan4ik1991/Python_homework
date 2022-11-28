""" Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число. """

n = int(input('Enter number N - '))
n_list = []
for item in range(-n,n+1,1):
    n_list.append(item)
print(n_list)
path = 'position.txt'
data = open(path, 'r')
for line in data:
 print(line)
data.close()
summa = n_list[1]+n_list[3]+n_list[6]
print(summa)

