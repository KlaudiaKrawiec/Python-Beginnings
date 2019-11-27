import random

def fff():
    for x in random.randrange(10):
        yield x

tab =  list(fff())