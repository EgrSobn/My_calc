import os
from prettytable import PrettyTable

def print_result(op1, op2, act, res):

    th = ['Num1','Operation', 'Num2', 'Result']
    td = [op1, act, op2, res]
    colums = len(th)

    table = PrettyTable(th)
    td_data = td[:]

    while td_data:
        table.add_row(td_data[:colums])
        td_data = td_data[colums:]
    
    print(table)