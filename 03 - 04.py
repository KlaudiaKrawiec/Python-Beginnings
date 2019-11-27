
file = open("NoEducation.txt","r")

n=1
for x in file:
    print(f'{n} {x}', end='')
    n += 1
file.close()