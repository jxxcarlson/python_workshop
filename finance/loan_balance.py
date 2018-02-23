# File: loan_balance.py

import sys, math

def round_off(x, digits):
    factor = 10**digits
    return round(x*factor)/factor

def future(present_balance, interest_rate, monthly_payment):
    balance = present_balance
    month = 0
    history = [(month, balance)]

    yearly_factor = (1 + interest_rate/100.0)
    monthly_factor = math.exp(math.log(yearly_factor)/12)

    while balance > 0 and (month < 1000):
        month = month + 1
        new_balance = monthly_factor*balance - monthly_payment
        if new_balance >= 0:
          balance = round_off(new_balance, 2)
          last_payment = 0
        else:
          balance = 0
          last_payment = new_balance + monthly_payment
        history.append((month, balance))
    return (history, last_payment)

def run(args):
    present_balance = float(args[1])
    interest_rate = float(args[2])
    monthly_payment = float(args[3])
    (history, last_payment) = future(present_balance, interest_rate, monthly_payment)

    for item in history:
        print item
    months_to_term = len(history)
    years_to_term = round_off(months_to_term/12.0, 1)
    total_payments = months_to_term*monthly_payment
    interest_paid = total_payments - present_balance
    print ""
    print "last payment = " + str(round_off(last_payment,2))
    print "years to term = " + str(years_to_term)
    print "total payments = " + str(total_payments)
    print "interest paid = " + str(interest_paid)


def message():
    "Usage: future_balance present_balance interest_rate years"

if len(sys.argv) == 4:
    run(sys.argv)
else:
    print message()
