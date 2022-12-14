import controller
import model_sum
def result_calc(result):
    with open('log.txt', 'a') as file:
         file.write(str(result)+'\n')

def write_example(x,y,symbol):
    with open('log.txt', 'a') as file:
        file.write(str(x) + str(symbol) + str(y) + str('='))