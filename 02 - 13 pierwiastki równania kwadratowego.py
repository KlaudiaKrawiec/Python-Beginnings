a = int(input('Podaj a dla ax^2 + bx + c = 0: '))
b = int(input('Podaj b dla ax^2 + bx + c = 0: '))
c = int(input('Podaj c dla ax^2 + bx + c = 0: '))

print(a,'x^2 + ', b ,'x + ', c ,' = 0')

delta = b**2 - 4*a*c


if delta < 0:
    print('Brak miejsc zerowych dla tego równania!')
elif delta == 0:
    x0 = (-b) / 2*a
    print('Równanie ma jeden pierwaistek! x0 = ', x0)
else:
    x1 = (-b - delta**(1/2)) / 2*a
    x2 = (-b + delta**(1/2)) / 2*a
    print('Równanie ma dwa pierwiasktki!! x1 = ', x1, 'x2 = ' , x2)