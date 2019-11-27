

file = open("macierz jednostkowa.txt", "w")

tab = [[0 for col in range(30)]for row in range(30)]

for y in range(30):
    tab[y][y] = 1
for i in tab:
    print(i)
    for j in i:
        file.write(f"{j} ")
    file.write("\n")
file.close()





    
