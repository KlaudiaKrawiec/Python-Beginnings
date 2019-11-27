a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))
c = int(input('Podaj trzecią liczbę: '))

tab = [a,b,c]
n = len(tab)

#sortowanie przez wstawianie isertionsort
for i in range(n):
    klucz = tab[i]
    nst = i - 1        # następny element (zaczynamy od pierwszego)
    while nst >= 0 and tab[nst]> klucz:
        tab[nst + 1] = tab[nst]
        nst -=1
    tab[nst + 1] = klucz

        
print ('Liczby w kolejności rosnącej: ', tab[0:3])
            
        
        
        