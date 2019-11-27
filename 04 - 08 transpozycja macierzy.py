from random import randrange as ra

#value = ra(10)
wymiar = ra(2,10)

print("Losowa macierz kwadratowa:")

mat = [[ra(10) for col in range(wymiar)]for row in range(wymiar)]

for col in mat:
    #print(col)
    for row in col:
        print(row,end=" ")
    print()
    
print("Macierz transponowana:")    
    
mat_t = [[0 for col in range(wymiar)]for row in range(wymiar)]

for i in range(wymiar):
    for j in range(wymiar):
        if j == i:
            mat_t[i][i] = mat[i][i]
        else:
            mat_t[i][j] = mat[j][i]
for c in mat_t:
    #print(c)
    for r in c:
        print(r, end=" ")
    print()