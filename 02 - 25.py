from random import randrange
wyniki = [0]*6
for i in range(100):
    wyniki[randrange(6)] += 1
print("Szóstka: {0}\nPiątka: {1}\nCzwórka: {2}\nTrójka: {3}\nDwójka: {4}\nJedynka: {5}".format(*wyniki))
      