"""
DniTygodnia = ['PN','WT','SR','CZW','PT','SB','ND']

nrDniaTygodnia = 2
LiczbaTygodni = 30//7 +1

print('|',end=' ')
for x in DniTygodnia:
    print(f'{x}',end=' | ')
print()

for t in range(LiczbaTygodni):
    print('\n|')
"""
nrDniaTygodnia = 2
kal = "| PN | WT | SR | CZ | PT | SB | ND |\n"
for i in range(nrDniaTygodnia):
    kal += "|    "
for i in range(1, 31):
    kal += "| " + str(i).rjust(2) + " "
    if ((i + nrDniaTygodnia)  % 7 == 0):
        kal += "|\n"
for i in range((5 - nrDniaTygodnia) % 7):
    kal += "|    "
kal += "|"
print(kal)