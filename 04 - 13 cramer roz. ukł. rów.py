
"""
2x+8y-z=5
3x+2y+5z=4
9x-6y+4z=1
"""
"""
AX = B
"""
def det(tab): #metoda sarrusa
    d1 = ((tab[0][0])*(tab[1][1])*(tab[2][2])) + ((tab[1][0])*(tab[2][1])*(tab[0][2])) + ((tab[2][0])*(tab[0][1])*(tab[1][2]))
    d2 = ((tab[0][2])*(tab[1][1])*(tab[2][0])) + ((tab[1][2])*(tab[2][1])*(tab[0][0])) + ((tab[2][2])*(tab[0][1])*(tab[1][0]))
    det = d1 - d2
    return det
def Change(Wi,p):
    for col in range(3):
        for row in range(3):
            if col == p:
                Wi[row][col] = matB[row][0]
            else:
                Wi[row][col] = matA[row][col]
    return Wi

matA = [[2,8,-1],[3,2,5],[9,-6,4]]

#matX = [[x],[y],[z]]
matB = [[5],[4],[1]]

W = matA
Wx = [[0 for x in range(3)] for y in range(3)]
Wy = [[0 for x in range(3)] for y in range(3)]
Wz = [[0 for x in range(3)] for y in range(3)]


Change(Wx,0)
Change(Wy,1)
Change(Wz,2)

detW = det(W)
detWx = det(Wx)
detWy = det(Wy)
detWz = det(Wz)

x = detWx/detW
y = detWy/detW
z = detWz/detW

print(f"x={x:4f} y={y:4f} z={z:4f}")

