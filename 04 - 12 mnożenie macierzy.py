from random import randrange as r
m = r(1,5)
n = r(1,5)
i = r(1,5)
j = r(1,5)

m = j #opcjonalne
n = i

A = [[r(10)for col in range(n)]for row in range(m)]
B = [[r(10)for col in range(j)]for row in range(i)]


if m == j and n == i:
    C = [[0 for col in range(j)]for row in range(m)]
    for wiersz in range(j):
        for kolumna in range(j):
            suma = 0
            for zm in range(i):
                suma += (A[wiersz][zm])*(B[zm][kolumna])

            C[wiersz][kolumna] = suma
            
    for col in A:
        for row in col:
            print(row, end=" ")
        print()
    print()
    for col in B:
        for row in col:
            print(row, end=" ")
        print()
    print()    
    for col in C:
        for row in col:
            print(row, end=" ")
        print()
    
    
else:
    print("Mnożenie macierzy nie może być wykonane!!! Złe wymiary")