import re
str = "pojazd KR932XV, prędkość 92km/h; pojazd WD49584, prędkość 76km/h; pojazd KR12145, prędkość 104km/h; pojazd KRA3451, prędkość 83km/h, pojazd LZX4039, prędkość 67km/h"
tab = [["KR932XV", "Piotr Wigierski"],["LZX4039", "Anna Maj"],["WD49584", "Andrzej Surmak"],["KR12145", "Zofia Dudek"],["KRA3451", "Stefan Nisko"]]
n = len(tab)

p1 = re.compile(r"[A-Z0-9]{7}")
p2 = re.compile(r" \d+")
rej = p1.findall(str)
iter = p2.findall(str)
pr = []
for x in iter:
    i = int(x)
    pr.append(i)

print("Imię i Nazwisko     Nr rejestrecyjny     Prędkość    Mandat")
print("                    pojazdu              km/h        zł")
print("-------------------------------------------------------------")

for r in range(n):
    for y in rej:
        if tab[r][0] == y:
            ind_pr = rej.index(y)
            p = pr[ind_pr]
            if p<=70:
                mandat = 200
                print(f"{(tab[r][1]):20} {y:18} {p:4d} {mandat:11d}")
            elif p>70 and p<=90:
                mandat = 350
                print(f"{(tab[r][1]):20} {y:18} {p:4d} {mandat:11d}")
            elif p>90:
                mandat = 1000
                print(f"{(tab[r][1]):20} {y:18} {p:4d} {mandat:11d}")

