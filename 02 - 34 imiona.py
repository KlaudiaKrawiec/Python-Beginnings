
imiona = ['Genowefa ','Onfury ','Celestyna ','Alojzy ','Pankracy ','Teofil ']

def lenght_e(x):
    return len(x)

print('Imiona: ', end=' ')
for x in imiona:
    print(f'{x}, ', end=' ')


imiona.sort(reverse=True, key=lenght_e)\
                          
print( '\nNajdłuższe imię: ', imiona[0])
    
    