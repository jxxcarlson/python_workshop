# File: future_balance.py

import sys

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

def run(args):
    present_balance = float(args[1])
    interest_rate = float(args[2])
    years = int(args[3])
    history = future(present_balance, interest_rate, years)
    for item in history:
        print item


def message():
    "Usage: future_balance present_balance interest_rate years"

if len(sys.argv) == 4:
    run(sys.argv)
else:
    print message()
