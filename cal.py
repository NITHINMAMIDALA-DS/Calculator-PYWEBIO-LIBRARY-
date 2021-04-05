#calculator operation


from pywebio.input import *
from pywebio.output import *

def mathematicaloperation():
    a = input("Enter the first number", type = FLOAT)
    b = input("Enter the second number", type=FLOAT)

    c = 0
    operation = radio("choose one operation", options =["+","*","/","%"])

    operation_name=""

    if operation=="+":
        operation_name="Addition"
        c = a+b

    elif operation=="*":
        operation_name ="Multiplication"
        c = a*b

    elif operation=="/":
        operation_name="Division"
        c=a/b

    elif operation=="%":
        operation_name="Modules"
        c = a%b

    put_text('the operation selected is : %s and the output is: %.1f' %(operation_name, c))

if __name__ =="__main__":
    mathematicaloperation()



