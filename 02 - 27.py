proby = 3
pin = "0805"
while(proby > 0):
    i = input("Podaj kod PIN: ")
    if i == pin:
        print("Gratuluję. ")
        break
    else:
        proby -= 1
        print("Błędny PIN. ")
else:
    print("Koniec prób. ")