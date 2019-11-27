
def matrix(wymiar):
    mat = [[0 for col in range(wymiar)]for row in range(wymiar)]
    
    for i in range(wymiar):
        mat[i][i] = 1
    
    for col in mat:
        # print(row)
        for row in col:
            print(row , end=" ")
        print()

matrix(2)
matrix(5)
matrix(10)
        