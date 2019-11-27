
pesel = str(input('Podaj swój nr pesel: '))
rok = '2018'

def wiek():
    if int(pesel[0:2]) >= int(rok[2:4]) and int(pesel[0:2]) <= 99:
        wiek = 100 - int(pesel[0:2]) + int(rok[2:4])
        print('Wiek: ', wiek)
            
    else:
        wiek = int(rok[2:4]) - int(pesel[0:2])
        print('Wiek:', wiek)

if len(pesel) == 11:
    print(pesel)
    if  int(pesel[9]) % 2 == 0:
        """
        Jeden element z listy: [0, 2, 4, 6, 8]
        """
        print('Płeć: Kobieta')
        wiek()
      
 
    elif int(pesel[9]) % 2 == 1:
        """
        Jeden el. z listy: [1, 3, 5, 7, 9]
        """
        print('Płeć: Mężczyzna')
        wiek()
else:
    print('Wprowadzony pesel jest niepoprawny!!!')
    