imie = input('Podaj swoje imie: ')

len = len(imie)

if imie[len - 1] == 'a':
    print('Jesteś kobietą')
else:
    print('Jesteś mężczyzną')