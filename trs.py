#!/usr/bin/python
# -*- coding: UTF-8 -*-

# terminal based trading record system

import sys
import time

from source.util import *

if sys.argv[1] == 'buy':
    args = read_argv_BS(sys.argv)
    print(buy(args))

if sys.argv[1] == 'sell':
    args = read_argv_BS(sys.argv)
    print(sell(args))

if sys.argv[1] == 'hold':
    hold()

if sys.argv[1] == 'history':
    history()

# if sys.argv[1] == 'history':

# if sys.argv[1] == 'ov':

if sys.argv[1] == 'ui':
    while True:
        print("[1] Buy\n[2] Sell\n[3] Read History\n[4] Check Holding\n[0] Exit")
        select = input("choose your action: ")
        if select == '1':
            symbol = input("Enter Symbol: ")
            value = input("Enter Value: ")
            price = input("Enter Price: ")
            argv = [0, "buy" ,symbol, value, price]
            args = read_argv_BS(argv)
            buy(args)
        elif select == '2':
            Symbol = input("Enter Symbol: ")
            value = input("Enter value: ")
            price = input("Enter price: ")
            argv = [0, "sell" ,symbol, value, price]
            args = read_argv_BS(argv)
            buy(args)
        elif select == '3':
            history()
        elif select == '4':
            hold()
        elif select == '0':
            sys.exit(0)
        else:
            print("\nPlease Enter number in rager[0 - 4]\n")
                
            
