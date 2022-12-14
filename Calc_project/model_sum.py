from fractions import Fraction
from view import get_value
from view import get_symbol
import logger
x=0
y=0
s=''

def get_method(a,b,c,d,symbol):
    global x
    global y
    global s
    s = symbol
    quest = str(input('enter rational or complex----'))
    if quest == 'complex':
        x = complex(a, b)
        print(x)
        y = complex(d, c)
        print(y)
        logger.write_example(x,y,symbol)
    if quest =='rational':
        x = Fraction(a, b)
        print(x)
        y = Fraction(d, c)
        print(y)
        logger.write_example(x,y,symbol)

def do_it():
    if s=='+':
        return x+y
    if s=='-':
        return x-y
    if s=='*':
        return x*y
    if s=='/':
        return x/y



