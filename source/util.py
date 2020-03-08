"""
helper functions
"""

import sys
import time
import os

def read_argv_BS(argv):
    localtime = time.strftime("%Y-%m-%d", time.localtime())
    unit = float(argv[3])/float(argv[4])
    args = dict( symbol=argv[2], value=argv[3], unit=unit,price=argv[4], time=localtime)
    return args

def buy(args):
    record = open("./record.txt", 'a+')
    stringFormat = "B|{}|{}|{:.2f}|{}|{}\n"
    stringOut = stringFormat.format(args["symbol"], args["value"], args["unit"], args["price"], args["time"])
    record.write(stringOut)        
    record.close()
    return stringOut

def sell(args):
    record = open("./record.txt", 'a+')
    stringFormat = "S|{}|{}|{:.2f}|{}|{}\n"
    stringOut = stringFormat.format(args["symbol"], args["value"], args["unit"], args["price"], args["time"])
    record.write(stringOut)        
    record.close()
    return stringOut

def history():
    record = open("./record.txt", "r")
    print('\33[31m' + "Action\t|Symbol\t|Value\t|Units\t|Price\t|Date\t|" + '\033[0m')
    # start value end value action market price units open open time close close time  P/L, P/L(%) value 
    for rows in record:
        row = rows.rstrip("\n")
        row = row.split('|')
        
        if row[0] == "B":
            row[0] = "Buy"
        elif row[0] == "S":
            row[0] = "Sell"
        else:
            continue

        printstring = '\33[37m' + "{0[0]}\t|{0[1]}\t|{0[2]}\t|{0[3]}\t|{0[4]}\t|{0[5]}\t|" + '\033[0m'
        print(printstring.format(row))
    record.close()

def hold():
    holding = open("./holding.txt", "r+")

    version = os.path.getsize("./record.txt")
    update_check = holding.readline()
    update_check = update_check.split('/')
    update_check[1] = int(update_check[1])
    if update_check[0] == '#':
        if update_check[1] == version:
            print("most updated")
        else:
            print("not updated")
            print("updating")
            update()
    else:
        print("Error")
        exit(0)

    print('\33[31m' + "Symbol".ljust(9, ' ') + "|Units".ljust(10, ' ') + "|AVG.Open".ljust(10, ' ') + "|P/L".ljust(10, ' ') + "|P/L(%)".ljust(10, ' ') + "|Value".ljust(10, ' ') + "|" + '\033[0m')
    for row_h in holding:
        row_h = row_h.rstrip("\n")
        row_h = row_h.split('|')
        stringOut = []
        for s in row_h:
            stringOut.append(s.rjust(9, ' '))

        if len(row_h) < 6:
            continue

        printstring = '\33[37m' + "{0[0]}|{0[1]}|{0[2]}|{0[3]}|{0[4]}|{0[5]}|" + '\033[0m'
        print(printstring.format(stringOut))

    holding.close()

def update():
    print("TBC")