def sum(*args):
    v = 0
    for a in args:
        v += a
    return v

def mult(*args):
    v = 1
    for a in args:
        v *= a
    return v