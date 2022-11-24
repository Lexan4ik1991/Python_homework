a = int(input('Введите день недели - '))
if a>0 and a<6:
    print('Будний день')

elif a>5 and a<8:
    print('Выходной день')
else :
    print ('Нет такого дня недели!')