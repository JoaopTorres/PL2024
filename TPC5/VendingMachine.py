import re

import ply.lex as lex

tokens = (
    'EURO',
    'CENT',
    'INSERT',
    'LIST',
    'BUY',
    'PRODID',
    'CHANGE'
)

t_EURO = r'[12]\s*€'
t_CENT = r'(50|20|10|5)\s*c'
t_INSERT = r'insert'
t_LIST = r'list'
t_BUY = r'buy'
T_PRODID = r'[0-9]+'
t_CHANGE = r'change'

t_ignore = ' \t'


def t_error(t):
    print(f"Invalid token: {t.value}")
    t.lexer.skip(1)


lexer = lex.lex()

total_money = 0

mode = 'N'

products = {
    1: {'name': 'Soda', 'cost': 130},
    2: {'name': 'Chips', 'cost': 180},
    3: {'name': 'Chocolate Bar', 'cost': 120},
    4: {'name': 'Water', 'cost': 70},
    5: {'name': 'M&M', 'cost': 120}
    # Add more products as needed
}


def insertMoney(coin):
    global total_money
    total_money += coin


def listProducts():
    print(products)


def buyProd(prodID):
    if prodID in products:
        pPrice = products[prodID]['cost']
        if total_money > pPrice:
            total_money -= pPrice
            print('Tak..clack..THUD.\n')
            print('Your %s has fallen.\nPick it up' % (products[prodID]['name']))
            print('You have ' + str(total_money) + '€')
        else:
            print('You have insuficient funds.')


def calcChange():
    ans = ''
    global total_money
    while total_money > 0:
        if total_money >= 200:
            total_money -= 200
            ans += '2€ '
        elif total_money >= 100:
            total_money -= 100
            ans += '1€ '
        elif total_money >= 50:
            total_money -= 50
            ans += '50c '
        elif total_money >= 20:
            total_money -= 20
            ans += '20c '
        elif total_money >= 10:
            total_money -= 10
            ans += '10c '
    print(ans)


while True:
    mode = 'N'
    user_input = input("Enter a command (insert, list, buy, change): ")
    lexer.input(user_input)
    for tokens in lexer:
        if tokens.type == 'INSERT':
            mode = 'I'
        elif tokens.type == 'EURO' and mode == 'I':
            insertMoney(int(tokens.value[:-1]) * 100)
            print(total_money)
        elif tokens.type == 'CENT' and mode == 'I':
            insertMoney(int(tokens.value[:-1]))
            print("Total->" + str(total_money))
        elif tokens.type == 'LIST':
            listProducts()
        elif tokens.type == 'BUY':
            mode = 'B'
        elif tokens.type == 'PRODID' and mode == 'B':
            buyProd(tokens.value)
        elif tokens.type == 'CHANGE':
            calcChange()
