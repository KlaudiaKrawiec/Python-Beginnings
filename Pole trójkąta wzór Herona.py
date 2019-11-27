a = int(input('Ramię trójkąta a ='))
b = int(input('Ramię trójkąta b = '))
c = int(input('Ramię trójkąta c = '))

if (a + b)>c and (a + c)>b and (b + c)>a:
    p = 1/2 * (a + b + c)
    PoleTrojkata = (p*(p-a)*(p-b)*(p-c))**(1/2)
    print('Pole Trójkąta a,b,c = ', PoleTrojkata)
else:
    print("Podane wymiary nie utworzą trójkąta! Wprowadź inne liczby.")
    



