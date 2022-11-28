#Напишите программу, 
#которая принимает на вход вещественное число и показывает сумму его цифр.(Сделать для строки)
# *Пример:*
#   - 6782 -> 23
#  - 0,56 -> 11

num = float(input('Enter number - '))
str_num = str(num)
str_num = str_num.replace('.', '')
lst_str = list(str_num)
lst_num = map(int, lst_str)
s= sum(lst_num)
print(s)


#result=0
#for i in converted_num:
  #  result+=i
  #  print(result)

