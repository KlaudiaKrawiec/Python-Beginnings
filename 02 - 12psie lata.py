forhuman = int(input('Podaj wiek psa w ludzkich latach: '))

if forhuman <= 2:
    fordog = forhuman*10,5
    print ('Wiek psa w psich latach: ', fordog)
else:
    fordog = 21 + (forhuman - 2)*4
    print ('Wiek psa w psich latach: ', fordog)