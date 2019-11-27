from time import time

start = time()

def liczby_pierwsze(n): # arg n wyznacza koniec przedziału z którego będą wyznaczane liczby pierwsze 

    liczba = 2  # l - kolejno liczby które są sprawdzane przez program (zaczynając od 2)

    for ilosc in range(n):       # pętla generująca liczby pierwsze dla danego przediału (zależnego od n)       
        for x in range(2,liczba-1):
            if liczba%x == 0:     # jeśli liczba jest podzielna przez x (które jest z przedziału [2 ; liczba -1] ) 
                liczba += 1   # to nie jest to liczba pierwsza
        return liczba         # jeśli warunek nie zostanie spełniony to jest to liczba pierwsza
        
print(liczby_pierwsze(6))            