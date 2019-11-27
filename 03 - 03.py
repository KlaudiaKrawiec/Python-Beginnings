
file = open("NoEducation.txt","r")

n=1
for x in file:
    if n == 2 or n == 3:
        print(x, end='')
    n += 1
file.close()