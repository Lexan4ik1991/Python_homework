#Напишите программу, которая принимает на вход координаты точки (X и Y), 
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
#в которой находится эта точка (или на какой оси она находится).
#Пример:

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3
 
x = int(input('Введите кординату x = '))
y = int(input('Введите кординату y = '))
if x!=0 and y!=0:
    if x>0 and y>0:
        print('1ая четверть')
    elif x<0 and y>0:
        print('2ая четверть') 
    elif x<0 and y<0:
        print('3я четверть')
    elif x>0 and y<0:
        print('4ая четверть')
else:
    print('Введена нулевая координата')





