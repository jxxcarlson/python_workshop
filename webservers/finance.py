# File: finance.py

from parse import parse

def round_off(x, digits):
    factor = 10**digits
    return round(x*factor)/factor

def future(present_balance, interest_rate, years):
    balance = present_balance
    history = [(0, balance)]
    factor = (1 + interest_rate/100.0)
    for k in range(1, years+1):
        balance = round_off(factor*balance, 2)
        history.append((k, balance))
    return history

def history2string(history):
    output = ""
    for (k, balance) in history:
        formatted_item = '   {:4d}  {:.2f}'.format(k, balance)
        output = output + formatted_item     + "\n"
    return output

def pre(str):
    return "<pre>\n\n" + str + "\n\n</pre>"

def reply(request):
    arg = parse(request)
    balance = float(arg['balance'])
    rate = float(arg['rate'])
    years = int(arg['term'])
    history = future(balance, rate, years)
    return pre(history2string(history))
