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

coinStrorage = {
    '2': {'quant': 0},
    '1': {'quant': 0},
    '50': {'quant': 0},
    '20': {'quant': 0},
    '10': {'quant': 1}

}

products = {
    'B-1': {'name': 'Soda', 'cost': 1.30, 'quant': 5},
    'A-1': {'name': 'Chips', 'cost': 1.80, 'quant': 10},
    'A-2': {'name': 'Chocolate Bar', 'cost': 1.20, 'quant': 6},
    'B-2': {'name': 'Water', 'cost': 0.70, 'quant': 7},
    'A-3': {'name': 'M&M', 'cost': 1.20, 'quant': 12}
    # Add more products as needed
}


def insertMoney(coin):
    global total_money
    total_money += coin
    if coin / 100 > 1:
        coinStrorage[str(int(coin / 100))]['quant'] += 1
    else:
        coinStrorage[str(coin)]['quant'] += 1


def listProducts():
    print(coinStrorage)
    for prodID in products:
        if products[prodID]['quant'] > 0:
            print("                ID:" + prodID + " | Name:" + products[prodID]['name'] + " | cost:" + str(
                products[prodID]['cost']))
        else:
            print("--UNAVAILABLE-- ID:" + prodID + " | Name:" + products[prodID]['name'] + " | cost:" + str(
                products[prodID]['cost']))


def buyProd(prodID):
    global total_money
    if prodID in products:
        pCount = products[prodID]['quant']
        if pCount > 0:
            pPrice = products[prodID]['cost'] * 100
            if total_money > pPrice:
                total_money -= pPrice
                products[prodID]['quant'] -= 1
                print('Tak..clack..THUD.\n')
                print('Your %s has fallen.\nPick it up' % (products[prodID]['name']))
            else:
                print('You have insufficient funds.')
        else:
            print("Product has no stock left.")


def calcChange():
    ans = ''
    noMoreChange = True
    global total_money
    while total_money > 0 and noMoreChange:
        if total_money >= 200 and coinStrorage['2']['quant'] > 0:
            total_money -= 200
            coinStrorage['2']['quant'] -= 1
            ans += '2€ '
        elif total_money >= 100 and coinStrorage['1']['quant'] > 0:
            total_money -= 100
            coinStrorage['1']['quant'] -= 1
            ans += '1€ '
        elif total_money >= 50 and coinStrorage['50']['quant'] > 0:
            total_money -= 50
            coinStrorage['50']['quant'] -= 1
            ans += '50c '
        elif total_money >= 20 and coinStrorage['20']['quant'] > 0:
            total_money -= 20
            coinStrorage['20']['quant'] -= 1
            ans += '20c '
        elif total_money >= 10 and coinStrorage['10']['quant'] > 0:
            total_money -= 10
            coinStrorage['10']['quant'] -= 1
            ans += '10c '
        elif total_money >= 10 and coinStrorage['10']['quant'] == 0:
            ans += '. Troco incompleto, fica a faltar: ' + str(total_money / 100) + 'c'
            noMoreChange = False
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
