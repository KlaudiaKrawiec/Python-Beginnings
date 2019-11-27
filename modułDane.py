import re


def czytajTekst(nazwaPliku):
    f = open(nazwaPliku, "r")
    tekst = f.read()
    return tekst

def pobierzDane(tekst):
    p = re.compile(r'\d[0-9\.]*')
    tab = p.findall(tekst)
    dane = []
    for x in range(len(tab)):
        l = float(tab[x])
        dane.append(l)
    return dane

        
