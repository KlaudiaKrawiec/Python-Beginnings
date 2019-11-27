
def utworz():
    matrix = [[0 for col in range(7)]for row in range(7)]
    return matrix

def zamien(matrix):
    n=len(matrix)
    for x in range(n):
        for y in range(n):
            if x==y:
                matrix[x][x]=1
            elif y==(n-1)-x:
                 matrix[x][y]=1
            elif y==0 or y==(n-1):
                matrix[x][y]=1
            elif (y==1 or y==(n-2)) and x!=0 and x!=(n-1):
                matrix[x][y]=1
            elif x==(n-1)//2:
                matrix[x][y]=1
    return matrix
def wyswietl(matrix):
    for row in matrix:
        for col in row:
            if col == 1:
                print("X", end=" ")
            else:
                print(" ", end=" ")
        print()

wyswietl(zamien(utworz()))