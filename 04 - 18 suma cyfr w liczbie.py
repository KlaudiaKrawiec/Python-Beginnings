
def suma(n): # rekursywnie
    if n == 0:
        return n
    else:
        return n%10 + suma(n//10)
"""
def suma(a): # iteracyjnie
    s=0
    while a>0:       #dopóki zostały jakieś cyfry
        s+=a%10     #dodaj ostatnią cyfrę (jedności)
        a//=10       #podziel liczbę przez 10
    return s
"""
print(suma(272))
