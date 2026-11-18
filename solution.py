import urllib.parse

def solve(value):
    return urllib.parse.quote(value, safe='')
