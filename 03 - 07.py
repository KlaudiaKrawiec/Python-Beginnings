
file = open("liczby.txt","r")

sum = 0

for x in file:
    i = int(x)
    sum += i
print(sum)

    
file.close()