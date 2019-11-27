sum = 0
ilosc = 0
x = int(input("Podaj liczbę: "))
while(x):
    ilosc += 1
    sum += x
    x = int(input("Podaj liczbę: "))
print("REZULTAT: Liczb={0},Suma={1},Średnia={2}".format(ilosc, sum, sum/ilosc))