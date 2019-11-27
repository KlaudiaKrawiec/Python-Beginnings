from random import randrange as r    

wiersze = r(1,10)
kolumny = r(1,10)
wartosc = r(10)

mat = [[r(10) for col in range(kolumny)]for row in range(wiersze)]

print("Losowa macierz:")

for col in mat:
    #print(x)
    for row in col:
        print(row, end=" ")
    print()

mat_t = [[0 for col in range(wiersze)]for row in range(kolumny)]

print("Macierz transponowana:")

for i in range(wiersze):
    for j in range(kolumny):
        mat_t[j][i] = mat[i][j]

for col in mat_t:
    for row in col:
        print(row, end=" ")
    print()