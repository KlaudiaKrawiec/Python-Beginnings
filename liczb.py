

for i in range(1,10):
    wzor = 1
    for j in range(2, i + 1):
        i *= str(j)
    print(i)