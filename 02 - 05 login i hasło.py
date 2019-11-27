
login = 'marek'
haslo = 'm-123'

plogin = input('Podaj login: ')    #PODANY LOGIN
phaslo = input('Podaj hasło: ')    #PODANE HASŁO

if plogin != login or phaslo != haslo:
    print('Nie udało ci się zalogować! \nPodane dane są nieprawidłowe')
else:
    print('Udało ci się zalogować do systemu!')
    