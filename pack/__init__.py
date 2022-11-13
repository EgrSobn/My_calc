from . import calcParams as CP
from . import calcLogging as CL
from . import calcPrint as CPR


def calc(op1, op2, act):
    match act:
        case "+":
            r = op1 + op2
        case "-":
            r = op1 - op2
        case "*":
            r = op1 * op2
        case "/":
            try:
                r = op1 / op2
            except ZeroDivisionError:
                print('На ноль делать нельзя, попробуйте снова')
                main_calc()
        case "^x":
            r = op1 ** op2
        case "%":
            r = op1 % op2
        case _:
            print('Что-то пошло не так, попробуйте снова')
            main_calc()

    try:
        CP.load_params()
    except:
        print('Не удалось загрузить параметры')
    res = CP.f1(r)
    print(res)
    CL.write_log(op1, op2, action=act, result=res)
    CPR.print_result(op1, op2, act, res)
            
def main_calc():
    print('Что я могу:\n Сложение "+"\n Вычитание "-"\n Умножение "*"\n Деление "/"\n Возведение в степень "^x"\n Деление с отсатком "%"')
    
    act = input('Сперва выберите действие (введите символ), или напишите Q для выхода\n')
    if act == "Q":
        exit()
    else:
        print('Введите последовательно 2 числа (порядок важен)')

    try:
      op1, op2 = float(input()), float(input())
    except:
      print('ERROR: Проверьте правильность введенных данных')
      main_calc()
    
    calc(op1, op2, act)