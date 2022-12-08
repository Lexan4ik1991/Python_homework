#Создайте программу для игры в ""Крестики-нолики"".

from random import*
print('---------------------------------------------------------')
print('Привет!Это игра Крестики-Нолики')
print('---------------------------------------------------------')

square = list(range(1,10))

def make_square(square): #Создаем нашу доску для игры
   print('-----------')
   for i in range(3):
      print("|", square[0+i*3], "|", square[1+i*3], "|", square[2+i*3], "|")
      print('-----------')

def make_input(player_choice): #функция выбора ввода
 while True:
    ans_choice=input('Выберите номер клетки:' +player_choice +'  ?')
    if not (ans_choice in '123456789'):
        print('Неверный ввод.Ввведите заново')
        continue
    ans_choice=int(ans_choice)
    if str(square[ans_choice-1])in 'XO':
        print('Клетка занята!Повторите ввод')
        continue
    square[ans_choice-1]=player_choice
    break
 
def win_combination(square): #функция определяет получилась ли победная комбинация
   win_position= ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for i in win_position:
       if square[i[0]] == square[i[1]] == square[i[2]]:
          return square[i[0]]
   return False
   


               
def its_game(square): #Сама игра
  name_one=str(input('Введите имя первого игрока - '))
  name_two=str(input('Введите имя второго игрока - '))
  num=randint(1,2) #Рандомом выбирается игрок
  if num==1:
    player1=name_one 
    player2=name_two 
  else:
    player1=name_two 
    player2=name_one 
  print(f'Ход будет выполнять игрок - {player1}')
  counter = 0
  win= False
  while not win:
   make_square(square)
   if counter %2==0:
      make_input('X')
   else:
      make_input('O')
   counter+=1
   if counter >4:
      tmp=win_combination(square)
      if tmp:
         if tmp =='X':
            print('---------') 
            print('Урааа!!')
            print('---------')
            print(player1)
         else:
            print('---------')
            print('Урааа!!')
            print('---------')
            print(player2)
         print('---------------------------------------------------------')
         print('Вы выйграли!!')
         print('---------------------------------------------------------')
         win=True
         break
   if counter == 9:
      print('Ничья')
      break
  make_square(square)  
  
its_game(square)

#P.S.
#Думаю сделать таблицу результатов, либо в файл,либо словарь


