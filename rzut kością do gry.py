import random        # Zaimportowanie generetora liczb losowych (pseudo-losowych)

rzut1 = random.randrange(1,7)  # rzut pierwszy
rzut2 = random.randrange(1,7)  # rzut drugi
rzut3 = random.randrange(1,7)  # rzut trzeci

print(rzut1, rzut2, rzut3)
print(rzut1 + rzut2 + rzut3)   # suma wartości rzutów