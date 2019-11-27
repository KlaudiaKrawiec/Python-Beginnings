
def czytajWspólczynniki():
    a = float(input("a="))
    b = float(input("b="))
    c = float(input("c="))
    print(f"Równanie kwadratowe postaci: {a}x^2 + ({b})x + ({c}) = 0")
    wsp = list((a,b,c))
    return wsp

def obliczDelte(tab):
    delta = tab[1]**2 - 4*tab[0]*tab[2]
    return delta

def obliczPierwiastki(tab):
    p_0 = []
    if obliczDelte(tab) < 0:
        return p_0
    elif obliczDelte(tab) == 0:
        x0 = -(tab[1])/(2*tab[0])
        p_1 = p_0.append(x0)
        return p_1
    else:
        x1 = -tab[1] - obliczDelte(tab)/(2*tab[0])
        x2 = -tab[1] + obliczDelte(tab)/(2*tab[0])
        p_2 = list((x1,x2))
        return p_2

def wyswietlPierwiastki(tab):
    if len(tab) == 0:
        print("Równanie nie ma pierwiastków")
    elif len(tab) == 1:
        print(f"Pierwiastek równania:        x0={tab[0]}")
    else:
        print(f"Pierwiastki równania:        x1={tab[0]} x2={tab[1]}")    
    


wyswietlPierwiastki(obliczPierwiastki(czytajWspólczynniki()))