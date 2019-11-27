suma = 0
srednia = 0
ilosc = 0
i = int(input('Podaj liczbę: '))
while(i):
    ilosc += 1
    suma += i
    srednia = suma/ilosc
    i = int(input('Podaj liczbę: '))
#    if i == 0:    #(z jakichś przyczyn niepotrzebne??)
#        break
print('Wyniki: Ilość liczb: {0} Suma liczb: {1} Średnia liczb: {2}'.format(ilosc,suma,srednia))

    