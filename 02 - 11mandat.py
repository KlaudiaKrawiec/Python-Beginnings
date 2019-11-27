
limit = int(input('Podaj limit prędkości (km/h): '))
speed = int(input('Podaj prędkość pojazdu (km/h): '))

if speed > limit:
    n = speed - limit # liczba przekroczonej prędkości
    if n <= 10:
        money = 5 * n
        print('Wysokość mandatu (zł): ', money)
    else:
        money = 50 + (n-10)*15
        print('Wysokość mandatu (zł): ', money)