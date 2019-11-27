print("Wprowadź punkt A: ")
xa = int(input("xa: "))
ya = int(input("ya: "))
print("Wprowadź punkt B: ")
xb = int(input("xb: "))
yb = int(input("yb: "))
print("Wprowadź punkt c: ")
xc = int(input("xc: "))
yc = int(input("yc: "))

tabABC = [[xa,ya,1],[xb,yb,1],[xc,yc,1]]

for w in tabABC:
    print(w)
    
det1 = (xa*yb)-(xb*ya)
det2 = (xa*yc)-(xc*ya)
det3 = (xb*yc)-(xc*yb)
detABC = det1 + det2 + det3

if detABC == 0:
    print("Punkty A,B,C są współliniowe")
else:
    print("Punkty A,B,C nie są współliniowe")

