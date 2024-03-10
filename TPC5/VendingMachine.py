import ply.lex as lex

tokens = (
    'EURO',
    'CENT',
    'INSERT',
    'LIST',
    'BUY',
    'PRODID',
    'CHANGE',
    'QUIT'
)

t_EURO = r'[12]\s*€'
t_CENT = r'(50|20|10|5)\s*c'
t_INSERT = r'insert'
t_LIST = r'list'
t_BUY = r'buy'
t_PRODID = r'[A-Z]-[1-9]?[0-9]+'
t_CHANGE = r'change'
t_QUIT = r'quit'

t_ignore = ' \t'


def t_error(t):
    print(f"Invalid token: {t.value}")
    t.lexer.skip(1)


lexer = lex.lex()

total_money = 0

mode = 'N'

products = {
    'B-1': {'name': 'Soda', 'cost': 1.30},
    'A-1': {'name': 'Chips', 'cost': 1.80},
    'A-2': {'name': 'Chocolate Bar', 'cost': 1.20},
    'B-2': {'name': 'Water', 'cost': 0.70},
    'A-3': {'name': 'M&M', 'cost': 1.20}
    # Add more products as needed
}


def insertMoney(coin):
    global total_money
    total_money += coin


def listProducts():
    print(products)


def buyProd(prodID):
    global total_money
    if prodID in products:
        pPrice = products[prodID]['cost'] * 100
        if total_money > pPrice:
            total_money -= pPrice
            print('Tak..clack..THUD.\n')
            print('Your %s has fallen.\nPick it up' % (products[prodID]['name']))
        else:
            print('You have insufficient funds.')


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
    print("Change: " + ans)


cicleB = True

while cicleB:
    mode = 'N'
    print("Available: " + str(total_money / 100) + "€")
    user_input = input("Enter a command (insert, list, buy, change, quit): ")
    lexer.input(user_input)
    for tokens in lexer:
        if tokens.type == 'INSERT':
            mode = 'I'
        elif tokens.type == 'EURO' and mode == 'I':
            insertMoney(int(tokens.value[:-1]) * 100)
        elif tokens.type == 'CENT' and mode == 'I':
            insertMoney(int(tokens.value[:-1]))
        elif tokens.type == 'LIST':
            listProducts()
        elif tokens.type == 'BUY':
            mode = 'B'
        elif tokens.type == 'PRODID' and mode == 'B':
            buyProd(tokens.value)
        elif tokens.type == 'CHANGE':
            calcChange()
            mode = 'C'
        elif tokens.type == 'QUIT' and mode == 'C':
            print('Thank you, goodbye')
            cicleB = False
        elif tokens.type == 'QUIT' and mode != 'C' and total_money > 0:
            print('Kaching, kachingKaching....')
            calcChange()
            print('Thank you, goodbye')
            cicleB = False
        elif tokens.type == 'QUIT' and mode != 'C' and total_money == 0:
            print('Thank you, goodbye')
            cicleB = False
