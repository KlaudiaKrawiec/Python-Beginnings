

string = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole,dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi,Prosto, długo, daleko, jako morza brzegi."

a = 0
y = 0
e = 0
o = 0
u = 0
i = 0
lenght = len(string)

for x in range(lenght):
    if string[x] == "a":
        a += 1
    elif string[x] == "y":
        y += 1
    elif string[x] == "e":
        e += 1
    elif string[x] == "o":
        o += 1
    elif string[x] == "u":
        u += 1
    elif string[x] == "i":
        i += 1
print(f"Ilość samogłosek: \na:{a} \ny:{y} \ne:{e} \no:{o} \nu:{u} \ni:{i}")

apr = a/lenght
ypr = y/lenght
epr = e/lenght
opr = o/lenght
ipr = i/lenght
upr = y/lenght

print(f"a% {apr:.2f}%\ny% {ypr:.2f}%\ne% {epr:.2f}%\no% {opr:.2f}%\nu% {upr:.2f}%\ni% {ipr:.2f}% ")