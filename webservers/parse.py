# File: parse.py

def parse(str):
    parts = str.lstrip("/").split("&")
    return dict(map(lambda x: x.split("="), parts))
