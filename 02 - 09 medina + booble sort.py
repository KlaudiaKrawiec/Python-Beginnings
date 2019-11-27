a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))
c = int(input('Podaj trzecią liczbę: '))

tab = [a,b,c]
n = len(tab)

# sortowanie bombelkowe
for x in range(n):
    ost = n - 1    # zaczynamy od ostatniej komórki
    while ost > x:            # od ostatniej szukanej 'x' (k-ty obrót pętli for)
        if tab[ost] < tab[ost - 1]: # jeśli ostatni elemnet tab jest mniejszy od poprzedzającego (ost-1)
            zam = tab[ost]         # zamienia miejscami (zamienia indexy dla elementow)
            tab[ost] = tab[ost - 1]
            tab[ost - 1] = zam
        ost -= 1

if n%2 == 1:
    mediana = (n - 1) // 2
    print('Mediana: ',tab[mediana])
