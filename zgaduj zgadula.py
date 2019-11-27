import random#zaimportowanie modułu generatora liczb losowych random

rzut = random.randrange(1,7)#wygenerowanie liczby z przedziału <1,6> (pod zmienną)

liczba_prob = 3
proba = 0
while proba < liczba_prob:
    zgadywanie = int(input("Wprowadź liczbę do 1 do 6: "))       #próba odgadniećia wprowadzenie z kalwiatury (input)
    if  zgadywanie >= 1 and zgadywanie <= 6 and rzut == zgadywanie:    #sprawdzenie instrukcją warunkową
        print('Udało ci się odgadnąć wylosowaną liczbę! \nBrawo!!! Wygrałeś!!!')
        break
    elif zgadywanie >= 1 and zgadywanie <= 6 and rzut != zgadywanie:
        print('Nie udało się :( Sprubuj jeszcze raz :) \n Próba:', proba, ' z trzech.' )
            
    else:
        print('Liczba z poza zakresu! Wprowadź inną liczbę. \nPróba: ',proba, ' z trzech.') 
    proba += 1
    
print('Koniec gry!')