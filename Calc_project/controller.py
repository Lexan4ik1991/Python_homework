#Кнопка
from statistics import mode
import model_sum as model
import view
import logger

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    value_c = view.get_value()
    value_d = view.get_value()
    symbol = str(view.get_symbol())
    model.get_method(value_a, value_b,value_c, value_d,symbol)
    result = model.do_it()
    view.view_data(result, "result")
    with open('log.txt', 'a') as file:
         file.write(str(result)+'\n')
    logger.result_calc(result)

