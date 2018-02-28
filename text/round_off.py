def round_off(x, digits):
    factor = 10**digits
    return round(x*factor)/factor
