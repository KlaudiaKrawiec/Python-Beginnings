
def matrix(wymiar):
    mat = [[0 for row in range(wymiar)]for col in range(wymiar)]
    
    for i in range(wymiar):
        mat[i][i] = 1
    
    for row in mat:
        # print(row)
        for col in row:
            print(col , end=" ")
        print()

matrix(2)
matrix(5)
matrix(10)
        