"""
x = '101'
y = '110'

x = list(x)
y = list(y)

s=[]
d=[]
for i in range(3):
    for ost in range(2,0,-1):
        if (x[ost]==1 and y[ost] == 0)or(x[ost]==0 and y[ost]==1):
            s[ost] = '1'
        elif x[ost]==0 and y[ost]==0:
            s[ost] = '0'
        else:
            s[ost] = '0'
            d[ost-1] = '1'
print(s)
"""
x, y, s = "101", "110", ""

#wyrównanie długości x i y poprzez dodanie 0 na poczatek krotszej (max. jedna z petli sie wykona):
for i in range(len(x) - len(y)):
    y = "0" + y
for i in range(len(y) - len(x)):
    x = "0" + x
    
c = 0
for a, b in zip(x[::-1], y[::-1]):
    sum = int(a) + int(b) + c
    s = str(sum % 2) + s
    c = (sum >= 2)
if c:
    s = "1" + s
