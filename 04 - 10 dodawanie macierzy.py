from random import randrange as r  

kolumny = r(1,11)
wiersze = r(1,11)

matrix1 = [[r(10) for col in range(kolumny)]for row in range(wiersze)]
matrix2 = [[r(10) for col in range(kolumny)]for row in range(wiersze)]
matrix_1sum2 = [[0 for col in range(kolumny)]for row in range(wiersze)]

for j in range(kolumny):
    for i in range(wiersze):
        matrix_1sum2[i][j] = matrix1[i][j] + matrix2[i][j]


for row in range(wiersze):
    for col in range(kolumny):
        print(matrix1[row][col], end=" ")
    print(end="    ")
    for col in range(kolumny):
        print(matrix2[row][col], end=" ")
    print(end="    ")
    for col in range(kolumny):
        print(f"{(matrix_1sum2[row][col]):2d}", end=" ")
    print()