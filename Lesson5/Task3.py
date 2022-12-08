#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
print('---------------------------------------------------------')
print('Реализация RLE алгоритма - сжатия и восстановления данных')
print('---------------------------------------------------------')
text=input('Введите буквы латинского алфавита - ')
def encode(string):
    result = ""
    i = 0
    while i<len(string):
         count = 1
         j = i
         while(j<len(string)-1):
             if string[j] == string[j+1]: 
                 count = count + 1
                 j += 1 
             else:
                 break
         result= result + str(count) + string[i]
         i = j + 1
    return result

result = encode(text)
print(text)
print('Сжатый текст',result)

def decode(result):
    decode_result=''
    count=''
    for item in result:
        if item.isdigit():
            count+=item
        else:
            decode_result+=item*int(count)
            count=''
    return decode_result
        

decode(result)   
decode_result= decode(result)
print('Восстановленный текст', decode_result)